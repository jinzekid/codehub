# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request

from spider_hexunpjt.items import SpiderHexunpjtItem
from spider_hexunpjt.ly_ProxyRequestUtil import proxyconfig, proxyrequest
from scrapy.http import Request


class MyhexunspdSpider(scrapy.Spider):
    name = 'myhexunspd'
    allowed_domains = ['hexun.com']
    # 设置要爬取用户的uid，为后续构造爬取网址做准备
    uid = "19940007"
    start_urls = ["http://19940007.blog.hexun.com/p1/default.html"]

    def start_requests(self):
        print(">>>进行第一次爬取<<<")
        # 首次爬取模拟成浏览器进行
        yield Request("http://"+str(self.uid)+".blog.hexun.com/p1/default.html",
                      headers={
                        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
                      })


    def parse(self, response):
        print(">>>parseing...<<<")
        item = SpiderHexunpjtItem()
        '''
            name = scrapy.Field() #存储文章名
            url  = scrapy.Field() #存储文章网址
            hits = scrapy.Field() #存储文章阅读数
            comment = scrapy.Field() #存储文章评论数
        '''
        item['name'] = response.xpath("//span["
                                      "@class='ArticleTitleText']/a/text("
                                      ")").extract()
        item['url'] = response.xpath("//span["
                                     "@class='ArticleTitleText']/a/@href").extract()

        # 接下来需要使用urllib和re模块获取博文的评论数和阅读数
        pat1 = '<script type="text/javascript" src="(http://click.tool.hexun.com/.*?)">'
        # hcrul为存储评论数和点击数的网址
        hcrul = re.compile(pat1).findall(str(response.body))[0]
        proxyconfig().install_globalOpener()
        data = proxyrequest(hcrul).get_data()
        print(data)
        # # pat2为提取文章阅读数的正则表达式
        pat2 = "click\d*?','(\d*?)'"
        # pat3为提取文章评论数的正则表达式
        pat3 = "comment\d*?','(\d*?)'"
        # 提取阅读数和评论数并分别赋值给item下的his和comment
        list_hits = (re.compile(pat2).findall(str(data)))
        list_comments = re.compile(pat3).findall(str(data))


        int_half = len(list_hits)
        item['hits'] = list_hits[0: int(int_half/2)]
        int_half = len(list_comments)
        item['comment'] = list_comments[0: int(int_half/2)]
        # 去重复操作
        '''
        tmp_list = item['comment']
        item['comment'] = list(set(tmp_list))
        '''
        print("==============")
        print(item)
        yield item

        # 提取博文列表的总页数
        pat4 = 'blog.hexun.com/p(.*?)/'
        # 通过正则表达式获取数据为一个列表，倒数第二个元素为总页数
        data2 = re.compile(pat4).findall(str(response.body))
        # 获取文章列表总页数
        if (len(data2) >= 2):
            totalurl = data2[-2]
        else:
            totalurl = 1

        print("总页数：" + totalurl)
        # # 进入for循环，依次爬取各博文列表页的博文数据
        # for i in range(2, 3):
        #     # 构造下一次要爬取的url，爬取一下页博文列表中的数据
        #     nexturl = "http://"+str(
        #         self.uid)+".blog.hexun.com/p"+str(i)+"/default.html"
        #     print("======================")
        #     print(nexturl)
        #     # 进行下一次爬取，下一次爬取仍然模拟成浏览器进行
        #     yield Request(
        #         nexturl,
        #         headers={
        #             'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) "
        #                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167"
        #                           " Safari/537.36"
        #         })







