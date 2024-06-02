# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBlogItem(scrapy.Item):
    html = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
