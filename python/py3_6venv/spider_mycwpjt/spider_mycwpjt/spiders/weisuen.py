# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from spider_mycwpjt.items import SpiderMycwpjtItem

class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']
    # rules = (
    #     Rule(LinkExtractor(allow='.shtml', allow_domains=('sohu.com')),
    #                        callback='parse_item',
    #          follow=True),
    # )

    rules = (
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'), allow_domains=('sohu.com')),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print("parse_item...")
        i = SpiderMycwpjtItem()
        i['name'] = response.xpath('/html/head/title/text()').extract_first()
        # i['link'] = response.xpath("//a/@href").extract_first()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
