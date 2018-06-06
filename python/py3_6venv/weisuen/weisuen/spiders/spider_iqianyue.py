# -*- coding: utf-8 -*-
import scrapy


class SpiderIqianyueSpider(scrapy.Spider):
    name = 'spider_iqianyue'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://iqianyue.com/']

    def parse(self, response):
        pass
