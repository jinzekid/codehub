# Author: Jason Lu
import urllib.request
from bs4 import BeautifulSoup
import time
req_header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding':'en-us',
    'Connection':'keep-alive',
    'Referer':'http://www.baidu.com/'
   }

req_timeout = 5
testUrl = "http://httpbin.org/get"
# testUrl = "http://www.whatismyip.com.tw"
testStr = "wahaha"

file_proxy = ''

file_output = open('proxy_out.txt', 'w')
# url = ""
# req = urllib2.Request(url,None,req_header)
# jsondatas = urllib2.urlopen(req,None,req_timeout).read()
# cookies = urllib2.HTTPCookieProcessor()

# 希望登录状态一直保持，使用Cookie处理
import http.cookiejar
# 使用http.cookiejar.CookieJar()创建CookieJar对象
cjar = http.cookiejar.CookieJar()
cookies = urllib.request.HTTPCookieProcessor(cjar)

checked_num = 0
grasp_num = 0

with open('download_4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # print(line)
        str_proxy_info = line.strip()
        protocol = 'HTTPS'
        # if protocol == 'HTTP' or protocol == 'HTTPS':
        ip, port = str_proxy_info.split(':')
        print('%s   :    %s' % (ip, port))
        proxyHandler = urllib.request.ProxyHandler({"http": '%s:%s'
                                                             % (ip, port)})
        # opener = urllib.request.build_opener(cookies, proxyHandler)
        opener = urllib.request.build_opener(proxyHandler, urllib.request.HTTPHandler)

        # 建立空列表，为了指定格式存储头信息
        headall = []
        for key, value in req_header.items():
            item = (key, value)
            headall.append(item)

        # 指定格式的headers信息添加好
        opener.addheaders = headall

        # opener.addheaders = [('User-Agent',
        #                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]

        # 创建全局默认的opener对象
        urllib.request.install_opener(opener)
        t1 = time.time()
        try:
            # req = opener.open(testUrl, timeout=req_timeout)
            # result = req.read().decode('utf-8')

            response = urllib.request.urlopen(testUrl, timeout=req_timeout)
            result = response.read().decode('utf-8')

            print(result)
            timeused = time.time() - t1
            pos = result.find(testStr)
            if pos > 1:
                file_output.write(protocol+"\t"+ip+"\t"+port+"\n")
                print(checked_num, grasp_num)
            else:
                continue
        except Exception as e:
            print(str(e))
            continue

        time.sleep(1)

    file_output.close()



# for page in range(1, 3):
#
#     for tr in trs[1:]:
#         tds = tr.find_all('td')
#         ip = tds[1].text.strip()
#         port = tds[2].text.strip()
#         protocol = tds[5].text.strip()
#         if protocol == 'HTTP' or protocol == 'HTTPS':
#             #of.write('%s=%s:%s\n' % (protocol, ip, port))
#             print('%s=%s:%s' % (protocol, ip, port))
#             grasp_num +=1
#             proxyHandler = urllib.request.ProxyHandler({"http": r'http://%s:%s' % (ip, port)})
#
#             opener = urllib.request.build_opener(cookies, proxyHandler)
#             opener.addheaders = [('User-Agent',
#                                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')]
#             t1 = time.time()
#             try:
#                 req = opener.open(testUrl, timeout=req_timeout)
#                 result = req.read()
#                 timeused = time.time() - t1
#                 pos = result.find(testStr)
#                 if pos > 1:
#                     file_output.write(protocol+"\t"+ip+"\t"+port+"\n")
#                     checked_num+=1
#                     print(checked_num, grasp_num)
#                 else:
#                     continue
#             except Exception as e:
#                 print(str(e))
#                 continue
# file_output.close()
# print(checked_num,grasp_num)