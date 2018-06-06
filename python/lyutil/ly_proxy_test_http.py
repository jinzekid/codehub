# Author: Jason Lu
import urllib.request
url = "http://httpbin.org/get"

import time
from lyutil.ly_ProxyRequestUtil import proxyrequest
from lyutil.ly_ProxyRequestUtil import proxyutil
from lyutil.ly_ProxyRequestUtil import proxyconfig

obj_putil = proxyutil('download_4.txt').parse_httpProxy()

for i in range(obj_putil.get_proxyLen()):
    obj_pconfig = proxyconfig(obj_putil.get_nextProxyInfo())
    obj_pconfig.install_globalOpener()
    obj_proxyrequest = proxyrequest(url, obj_putil, obj_pconfig)
    data = obj_proxyrequest.get_data()
    print(data)
    print(">>>等待1.5秒再次请求<<<")
    time.sleep(1.5)
    print()








