# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request, FormRequest

class LoginspdSpider(scrapy.Spider):
    name = 'loginspd'
    header = {'User-Agent':
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
              }
    # 登录豆瓣 ,jd
    allowed_domains = ['douban.com', 'jd.com']

    # douban请求
    '''
    def start_requests(self):  # 用start_requests()方法,代替start_urls
        """第一次请求一下登录页面，设置开启cookie使其得到cookie，设置回调函数"""
        return [Request('https://accounts.douban.com/login',
                    meta={'cookiejar': 1}, callback=self.parse,
                        headers=self.header)]
                        
    def parse(self, response):
        print(">>>parsing<<<")
        # 登录时候有时网页有验证码，有时网页没有验证码
        captcha = response.xpath('//ing[@id="captcha_image"].@src').extract()
        if len(captcha) > 0:
            print("此时有验证码")
            localpath = 'captcha.png'
            urllib.request.urlretrieve(captcha[0], filename=localpath)
            print("请查看本地图片captch.png并输入对应验证码")
            # 通过input输入验证码
            captcha_value = input()
            
            data = {
                "form_email": "514432996@qq.com",
                "form_password": "kid1412ly",
                "captcha-solution": captch_value,
                "redir": "https://www.douban.com/people/167021347/",
            }
        else:    
            data = {
                "form_email": "514432996@qq.com",
                "form_password": "kid1412ly",
                "redir": "https://www.douban.com/people/167021347/",
            }
        
        print("登录中...")
        # 通过FormRequest.form_response()进行登录
        return [FormRequest.from_response(response,
                                          headers=self.header,
                                          formdata=data,
                                          callback=self.next,
                                          )]
    '''

    # jd请求 没成功
    def start_requests(self):  # 用start_requests()方法,代替start_urls
        """第一次请求一下登录页面，设置开启cookie使其得到cookie，设置回调函数"""
        return [Request('https://passport.jd.com/uc/login',
                    meta={'cookiejar': 1}, callback=self.parse,
                        headers=self.header)]


    def parse(self, response):
        print(">>>parsing<<<")
        data = {
            "loginname": "doctorhsly",
            "nloginpwd": "kid1412ly_luyang",
            "redir": "https://home.jd.com/",
        }

        print("登录中...")
        # 通过FormRequest.form_response()进行登录
        return [FormRequest.from_response(response,
                                          headers=self.header,
                                          formdata=data,
                                          callback=self.next,
                                          )]


    def next(self, response):
        print("此时已经登录完成并爬取了个人中心的数据")

        xtitle = "/html/head/title/text()"

        print(str(response.body))
        str_title = response.xpath(xtitle).extract()
        print(str_title)
