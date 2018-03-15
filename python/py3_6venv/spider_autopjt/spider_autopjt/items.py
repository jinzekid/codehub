# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderAutopjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name   = scrapy.Field() #商品名称
    price  = scrapy.Field() #商品价格
    link   = scrapy.Field() #商品链接
    comnum = scrapy.Field() #商品评论数
    pass
