# Author: Jason Lu

import gevent
import urllib, json
from urllib import request
# 引入monkey包
from gevent import monkey
# 把当前程序的所有的io操作单独的做上标记，然后进行并发
monkey.patch_all()

def func(url):
    str_url =url
    print(str_url)

    content = urllib.request.urlopen(str_url, timeout=None)
    print("get data length:", (len(content.read())))
    # f = open("url.html", "wb")
    # f.write(content.read())


# 使用协程
gevent.joinall([
    gevent.spawn(func, "http://www.cnblogs.com/alex3714/articles/5248247.html"),
    gevent.spawn(func, "http://www.python.org"),

])

