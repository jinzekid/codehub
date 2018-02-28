# Author: Jason Lu
import urllib.request
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
# proxy = '122.242.93.39:43023'
# proxy_handler = ProxyHandler({
#     'http': proxy, 'https': proxy
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('http://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

url = "http://httpbin.org/get"
# htmlsource = urllib.request.FancyURLopener({"http":"http://122.242.93.39:43023",
#                                             "https":"https://122.242.93.39:43023"})\
#                             .open(url).read().decode("utf-8")
# print(htmlsource)

import time
from lyutil.ly_ProxyRequestUtil import proxyrequest
from lyutil.ly_ProxyRequestUtil import proxyutil
from lyutil.ly_ProxyRequestUtil import proxyconfig

obj_putil = proxyutil('download_4.txt').do_parseHttpProxy()

# obj_pconfig = proxyconfig(obj_putil.get_nextProxyInfo())
# obj_pconfig.do_installGlobalOpener()

for i in range(obj_putil.get_proxyLen()):
    obj_pconfig = proxyconfig(obj_putil.get_nextProxyInfo())
    obj_pconfig.do_installGlobalOpener()
    obj_proxyrequest = proxyrequest(url, obj_putil, obj_pconfig)
    data = obj_proxyrequest.getdata()
    print(data)
    print(">>>等待1.5秒再次请求<<<")
    time.sleep(1.5)
    print()






