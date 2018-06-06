# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderTaishaHsbcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()
    topic_d = scrapy.Field()
    note_d  =scrapy.Field()
    topic = scrapy.Field()
    note = scrapy.Field()
    pass
