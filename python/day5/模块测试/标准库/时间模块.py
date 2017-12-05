# Author: Jason Lu

import time

help(time)
# help(time.gmtime)

print(time.time()) # 单位是秒，从1970年开始
print(time.gmtime()) # 传入本地时间，得到的是UTC时区结果
print(time.localtime()) # 传入本地时间，得到本地时区结果

print(time.timezone)
print(time.altzone)

# 时间戳转换tuple
print(time.gmtime(1634234324))
x = time.gmtime(1634234324)

# 时间tuple转换为时间戳
print(time.mktime(x))

# 时间tuple转换字符串
print(time.strftime("%Y-%m-%d %H:%M:%S"), time.gmtime(1634234324))

# 字符串转换时间tuple
ret = time.strptime("2017-12-05 10:02:31", "%Y-%m-%d %H:%M:%S")
print(ret)

print(time.asctime()) # Tue Dec  5 10:57:26 2017
print(time.ctime(1634234324)) # Fri Oct 15 01:58:44 2021


import datetime
print(datetime.datetime.now()) # 获取当前时间
print(datetime.datetime.now() + datetime.timedelta(-3)) # 前三天
print(datetime.datetime.now() + datetime.timedelta(3)) # 后三天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) # 后三小时
print(datetime.datetime.now() + datetime.timedelta(hours=-3)) # 前三小时
print(datetime.datetime.now() + datetime.timedelta(minutes=10)) # 后10分钟
print(datetime.datetime.now() + datetime.timedelta(minutes=-10)) # 前10分钟




