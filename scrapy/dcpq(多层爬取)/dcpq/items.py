# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DcpqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    pubTime = scrapy.Field()
    picture = scrapy.Field()
    content = scrapy.Field()
    url=scrapy.Field()
    
    pass
