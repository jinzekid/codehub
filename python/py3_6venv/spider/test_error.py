# Author: Jason Lu
import urllib.request
import urllib.error

try:
    data = urllib.request.urlopen('http://blog.csdn.net')
    print(data.code)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)


import urllib.error
import urllib.request
try:
    urllib.request.urlopen('http://blog.baidusss.net')
# except urllib.error.HTTPError as e:
except urllib.error.URLError as e:
    print(e.reason)


# 合并后处理异常
import urllib.request
import urllib.error

try:
    urllib.request.urlopen('http://blog.baidusss.net')
except urllib.error.HTTPError as e:
    print(e.reason)
    print(e.code)
except urllib.error.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)








