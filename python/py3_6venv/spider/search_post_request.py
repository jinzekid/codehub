# Author: Jason Lu
import urllib.request
import urllib.parse

url = 'http://www.iqianyue.com/mypost/'
postdata = urllib.parse.urlencode({
    "name": "ceo@iqianyue.com",
    "pass": "aA123456"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent',
               "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
data = urllib.request.urlopen(req).read()

fhandle = open('6.html', 'wb')
fhandle.write(data)
fhandle.close()


# 124.133.97.17	8118
















