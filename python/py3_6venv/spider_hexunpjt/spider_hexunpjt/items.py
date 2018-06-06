# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SpiderHexunpjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() #存储文章名
    url  = scrapy.Field() #存储文章网址
    hits = scrapy.Field() #存储文章阅读数
    comment = scrapy.Field() #存储文章评论数
    pass
