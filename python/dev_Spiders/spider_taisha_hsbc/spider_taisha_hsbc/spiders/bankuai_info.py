# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from scrapy.http import Request
from spider_taisha_hsbc.items import SpiderTaishaHsbcItem

class BankuaiInfoSpider(scrapy.Spider):
    name = 'bankuai_info'
    allowed_domains = ['bbs.taisha.org']
    start_urls = ['http://bbs.taisha.org/']

    def start_requests(self):
        print(">>>进行第一次爬取<<<")
        # 首次爬取模拟成浏览器进行
        url = self.start_urls[0]
        print(url)
        yield Request(url,
                      headers={
                        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
                      })


    def parse(self, response):
        print(">>>parsing...<<<")
        item = SpiderTaishaHsbcItem()

        # print(str(response.body))
        # 网页保存
        obj_file = open('bankuai.html', 'wb')
        obj_file.write(response.body)
        obj_file.close()

        pat = "<em>.?*</em>"
        # 解析信息
        item['name'] = response.xpath("//td["
                                      "@class='fl_g']/dl/dt/a4/text()"
                                      "").extract()
        item['topic_d'] = response.xpath("//td[@class='fl_g']/dl/dd/em[1]"
                                            "").extract()

        item['note_d'] = response.xpath("//td[@class='fl_g']/dl/dd/em[2]"
                                            "").extract()
        print("=====================")
        yield item
