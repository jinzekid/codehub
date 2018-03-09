# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeisuenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urlname = scrapy.Field()
    urlkey  = scrapy.Field()
    urlcr   = scrapy.Field()
    urladdr = scrapy.Field()
    pass


weisuen = WeisuenItem(urlname= "weiwei",
                      urlkey = "keykey",
                      urlcr  = "crcr",
                      urladdr= 'addraddr')

print(weisuen["urlname"])
