# Author: Jason Lu
import re
import urllib.request

def getlink(url):
    headers = ('User-Agent',
                   "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    print(data)
    # 根据需求构建好链接表达式
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    # 去除重复元素
    link = list(set(link))
    return link

# 要爬取的网页链接
url = 'https://www.cnblogs.com/skiler/p/6687337.html'
# 获取对应网页中包含的链接地址
linklist = getlink(url)
print(len(linklist))
# for循环分别遍历输出获取到的链接地址
for link in linklist:
    print(link[0])