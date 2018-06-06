# Author: Jason Lu

import re, time, random

from lyutil.ly_ProxyRequestUtil import proxyrequest

proxies = {'http': 'http://127.0.0.1:8888'}

url = "https://video.coral.qq.com/varticle/1472528692/comment/v2?cursor=0"

def getContent(url):

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
        "Connection": "keep-alive",
        "referer": "qq.com/",
        "Accept-Encoding": "utf-8"
    }

    str_url = url
    print(str_url)
    data = proxyrequest(str_url, header=headers, saveCookie=True).getdata()
    print(data)

    data_new = str(data).replace("true", "True")

    json_data = eval(data_new)
    # 获取oriCommList
    commlistpat = '"oriCommList":(.*?)],'
    # 获取用户列表
    userlistpat = '"userList":(.*?),"targetInfo"'

    commlist = re.compile(commlistpat, re.S).findall(data_new)
    userlist = re.compile(userlistpat, re.S).findall(data_new)

    print()
    list_user = list(userlist)
    str_list_user = list_user[0]

    list_comm = list(commlist)
    str_list_comm = list_comm[0]
    # print(str_list_comm)
    # print(list_comm)

    userlistpat2 = '"(\d{9}|\d{8})":(.*?)}' #用户id可能8位或者9位
    list_user = re.compile(userlistpat2, re.S).findall(str_list_user)
    commlistpat2 = '(.*?)},'
    list_comm = re.compile(commlistpat2, re.S).findall(str_list_comm)

    for v in list_comm:
        print(v)
    print()
    for v in list_user:
        print(v)


getContent(url)

'''fdsfdsdddddfdsfdsdddddfdsfdsdddddfdsfdsdddddfdsfdsdddddfdsfdsdddddfdsfdsddddd
fdsfdsddddd'''