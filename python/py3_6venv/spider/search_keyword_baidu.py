# Author: Jason Lu
import urllib.request

str_keyword = input('输入关键词--->:')
str_keyword = urllib.request.quote(str_keyword)
url = 'https://www.baidu.com/s?ie=utf-8&tn=SE_PSStatistics_p1d9m0nf&wd=' + str_keyword
print(url)

# 使用build_opener()修改报头
headers = ("User-Agent",
           "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()

# req = urllib.request.Request(url)
# data = urllib.request.urlopen(req).read()

fhandle = open('4.html', 'wb')
fhandle.write(data)
fhandle.close()
