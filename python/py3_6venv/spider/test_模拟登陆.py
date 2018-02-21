# Author: Jason Lu
import urllib.request
import urllib.parse

url = 'https://www.douban.com/accounts/login'
postdata = urllib.parse.urlencode({
    "form_email": "514432996@qq.com",
    "form_password": "kid1412ly"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent',
               "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
data = urllib.request.urlopen(req).read()

fhandle = open('login_douban.html', 'wb')
fhandle.write(data)
fhandle.close()