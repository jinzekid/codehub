# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from scrapy.http import Request
from spider_jd_phone.items import SpiderJdPhoneItem


class JdPhoneSpider(scrapy.Spider):
    name = 'jd_phone'
    allowed_domains = ['jd.com']
    str_keyword = '手机京东自营'
    encode_keyword = urllib.request.quote(str_keyword)
    url = 'https://search.jd.com/Search?keyword=' + encode_keyword + '&enc=utf-8&qrst' \
                                                                  '=1&rt' \
                                                                  '=1&stop=1&spm=2.1.0&vt=2&page=1&s=1&click=0'
    # start_urls = [url]

    # def start_requests(self):
    #     print(">>>进行第一次爬取<<<")
    #     print("爬取网址：%s" % self.url)
    #     yield Request(self.encode_url,
    #                   headers={
    #                     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) "
    #                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
    #                   })

    # 设置要爬取用户的uid，为后续构造爬取网址做准备
    # uid = "19940007"
    # start_urls = ["http://19940007.blog.hexun.com/p1/default.html"]

    def start_requests(self):
        print(">>>进行第一次爬取<<<")
        # 首次爬取模拟成浏览器进行
        # yield Request(
        #     "http://" + str(self.uid) + ".blog.hexun.com/p1/default.html",
        #     headers={
        #         'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) "
        #                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
        #     })

        url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&enc=utf-8&qrst=1&rt%27=1&stop=1&spm=2.1.0&vt=2&page=1&s=1&click=0"
        print(url)
        yield Request("https://search.jd.com/Search?keyword=" +
                      self.str_keyword + "&enc=utf-8&qrst=1&rt'=1&stop=1&spm=2.1.0&vt=2&page=1&s=1&click=0",
                      headers={
                        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
                      })


    def parse(self, response):
        print(">>>parsing...<<<")
        item = SpiderJdPhoneItem()
        # print(str(response.body))

        file_object = open('test.html', 'wb')
        file_object.write(response.body)
        file_object.close()

        item['price'] = response.xpath("//div["
                                       "@class='p-price']//i/text()").extract()
        item['name'] = response.xpath("//div[@class='p-name "
                                      "p-name-type-2']//em").extract()
        print("获取item：{}".format(item))
        print("长度：%s" % len(item['price']))
        print("长度：%s" % len(item['name']))

        print("=====================")
        yield item

