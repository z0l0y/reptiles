# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import re
from datetime import datetime

import html2text
from bs4 import BeautifulSoup
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BlogPipeline:
    def __init__(self):
        self.file_path = None
        self.output_dir = None
        self.fp = None
        self.h2t = html2text
        self.prefix = "https://z0l0y.github.io/"

    def open_spider(self, spider):
        self.output_dir = 'blog_posts'
        os.makedirs(self.output_dir, exist_ok=True)

    def process_item(self, item, spider):
        try:
            title = re.sub(r'</?[^>]+>', '', item['title'])
            published_at = datetime.strptime(item['date'], '%Y/%m/%d')
            file_path = os.path.join(self.output_dir, published_at.strftime('%Y'), published_at.strftime('%m'),
                                     published_at.strftime('%d'),
                                     f"{title}.md")
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            markdown_content = self.h2t.html2text(item['html'])
            markdown_content = re.sub(r'!\[(.*?)]\((.*?)\)', r'![\1](https://z0l0y.github.io/\2)', markdown_content)
            with open(file_path, 'w', encoding='utf-8') as fp:
                fp.write(markdown_content)
        except (ValueError, KeyError):
            pass
        return item
