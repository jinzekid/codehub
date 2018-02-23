# Author: Jason Lu
import re, time, random

from lyutil.ly_ProxyRequestUtil import proxyrequest

proxies = {'http': 'http://127.0.0.1:8888'}

def getContent():
    # 循环爬取各页的文章链接
    str_url = "http://news.163.com/16/0825/09/BVA8A9U500014SEH.html"
    print(str_url)
    data = proxyrequest(str_url, proxy=proxies, saveCookie=True).getdata(b_needbyte=True)
    print(data)
    fhandle = open('1.html', 'wb')
    fhandle.write(data)
    fhandle.close()

# getContent()

def getContent2():
    # 循环爬取各页的文章链接
    str_url = "http://news.163.com/16/0825/09/BVA8A9U500014SEH.html"

    headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
                "Connection": "keep-alive",
                "referer": "http://www.163.com/",
                "Accept-Encoding": "utf-8"
               }

    data = proxyrequest(str_url, proxy=proxies, header=headers, saveCookie=True).getdata(b_needbyte=True)
    print(data)
    fhandle = open('2.html', 'wb')
    fhandle.write(data)
    fhandle.close()

getContent2()