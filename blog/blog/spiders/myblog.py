import os
import re
from datetime import datetime
from urllib.parse import urlparse

import scrapy
from html2text import HTML2Text
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from blog.items import ScrapyBlogItem


class MyblogSpider(scrapy.Spider):
    name = "myblog"
    allowed_domains = ["z0l0y.github.io"]
    start_urls = ["https://z0l0y.github.io"]
    global year
    base_url = 'https://z0l0y.github.io'

    def __init__(self, year=2024, *args, **kwargs):
        super(MyblogSpider, self).__init__(*args, **kwargs)
        self.year = year

    def parse(self, response):
        global valid_src_list, name
        os.makedirs("blog_posts", exist_ok=True)
        src_list = response.xpath('//div[@class="card"]//a')
        title_list = response.xpath('//span[@class="card-title"]')

        valid_src_list = []
        valid_name_list = []
        unique_src_set = set()
        unique_name_set = set()

        for src in src_list:
            href = src.xpath('./@href').extract_first()
            if re.match(rf'/{self.year}/\d+/\d+/\d+/', href) and href not in unique_src_set:
                valid_src_list.append(href)
                unique_src_set.add(href)
            if re.match(rf'/{self.year}/\d+/\d+/([^/]*)/?', href) and href not in unique_src_set:
                valid_src_list.append(href)
                unique_src_set.add(href)
        for name in title_list:
            if name not in unique_name_set:
                valid_name_list.append(name)
                unique_name_set.add(name)

        for href, title in zip(valid_src_list, valid_name_list):
            url = self.base_url + str(href)
            name = title.css('::text').get()
            parsed_url = urlparse(url)
            time = '/'.join(parsed_url.path.strip('/').split('/')[:3])
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name, 'time': time})

    def parse_second(self, response):
        body_list = response.xpath('//div[@class="card-content article-card-content"]')
        if body_list:
            body_html = body_list.get()
            title = response.meta['name']
            date = response.meta['time']
            content = ScrapyBlogItem(html=body_html, title=title, date=date)
            print("\033[31m" + body_html + "\033[0m")
            yield content
