# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy.http import Request
from spider_qtpjt.items import SpiderQtpjtItem

class QtspdSpider(scrapy.Spider):
    name = 'qtspd'
    allowed_domains = ['58pic.com']
    start_urls = [
        'http://www.58pic.com/piccate/3-0-0-1.html'
    ]

    def parse(self, response):
        print(">>>parsing...<<<")
        item = SpiderQtpjtItem()
        # 构建提取缩略图网址的正则表达式
        paturl = "(http://pic.qiantucdn.com/58pic/.*?).jpg"
        # 提取对应图片网址
        list_picurl = re.compile(paturl).findall(str(response.body))
        item['picurl'] = list(set(list_picurl))
        # print(item["picurl"])

        print("====================")
        # 构造出提取图片名的正则表达式，以方便构造出本地的文件名
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
        # 提取互联网中图片名
        list_picid = re.compile(patlocal).findall(str(response.body))
        item["picid"] =list(set(list_picid))
        # print(item["picid"])

        print("====================")
        print(item)
        yield item

        # 通过for循环依次遍历1到200页图片列表页
        for i in range(1, 50):
            nexturl = "http://www.58pic.com/piccate/3-0-0-"+str(i)+".html"
            yield Request(nexturl, callback=self.parse)