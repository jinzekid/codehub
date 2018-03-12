# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from spider_myxml.items import SpiderMyxmlItem


class PersonSpider(XMLFeedSpider):
    name = 'person'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/test.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'person' # change it accordingly

    def parse_node(self, response, selector):
        i = SpiderMyxmlItem()
        i['link'] = selector.xpath('/person/email/text()').extract()
        print(i['link'])
        # i = {}
        #i['url'] = selector.select('url').extract()
        #i['name'] = selector.select('name').extract()
        #i['description'] = selector.select('description').extract()
        return i
