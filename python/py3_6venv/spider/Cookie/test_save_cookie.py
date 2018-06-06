# Author: Jason Lu

import urllib.request
import urllib.parse

data_post = urllib.parse.urlencode({
    'username':'doctorhsly',
    'password':'201718'
}).encode('utf-8')
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LeWQG"

req = urllib.request.Request(url, data=data_post)
req.add_header('User-Agent',
               "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")

# 希望登录状态一直保持，使用Cookie处理
import http.cookiejar
# 使用http.cookiejar.CookieJar()创建CookieJar对象
cjar = http.cookiejar.CookieJar()
# 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
# 将opener安装为全局
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()

fhandle = open("3.html", "wb")
fhandle.write(data)
fhandle.close()


url2 = "http://bbs.chinaunix.net/"
req2 = urllib.request.Request(url2, data_post)
req2.add_header('User-Agent',
               "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
data2 = urllib.request.urlopen(req).read()
fhandle = open('4.html', "wb")
fhandle.write(data2)
fhandle.close()
