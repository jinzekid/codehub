# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from spider_autopjt.items import SpiderAutopjtItem

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/childrensbooks/01.41.00.00.00.00-24hours-0-0-1-1-bestsell']

    def parse(self, response):
        item = SpiderAutopjtItem()

        item['name'] = response.xpath("//div["
                                     "@class='name']/a/text()").extract()

        item['price'] = response.xpath("//span["
                                       "@class='price_n']/text()"
                                       "").extract()
        item['link'] = response.xpath("//div["
                                     "@class='name']/a/@href").extract()
        item['comnum'] = response.xpath("//div["
                                      "@class='star']/a/text("
                                        ")").extract()
        yield item

        # for i in range(1, 4):
        #     url = 'http://bang.dangdang.com/books/childrensbooks/01.41.00.00' \
        #           '.00.00-24hours-0-0-1-'+str(i)+'-bestsell'
        #     print('spider crawl url: %s' %url)
        #     yield Request(url, callback=self.parse)
