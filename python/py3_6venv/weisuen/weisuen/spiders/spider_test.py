# -*- coding: utf-8 -*-
import scrapy


class SpiderTestSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://iqianyue.com/']

    def parse(self, response):
        pass
