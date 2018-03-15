# -*- coding: utf-8 -*-
import scrapy
from spider_mypjt.items import SpiderMypjtItem

class MyspdSpider(scrapy.Spider):
    name = 'myspd'
    allowed_domains = ['sina.com.cn']
    start_urls = [
        'http://www.sina.com.cn/',
        'http://tech.sina.com.cn/d/s/2016-09-17/doc-ifxvyqwa3324638.shtml'
    ]

    def parse(self, response):
        item = SpiderMypjtItem()

        item['title'] = response.xpath('/html/head/title/text()').extract_first()
        item['key'] = response.xpath("//meta["
                                     "@name='keywords']/@content").extract_first()

        print(item['title'])
        yield item #注意这里需要yield item才能解析
