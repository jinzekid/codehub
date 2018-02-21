# Author: Jason Lu
import urllib.request
filename = urllib.request.urlretrieve("http://edu.51cto.com", filename="2.html")
file = urllib.request.urlopen("http://www.baidu.com")
# print(file.info())
# print(file.getcode())
# print(file.geturl())

# url编码, 用于中文以及特殊字符
# encode_url = urllib.request.quote("http://www.sina.com.cn")
# print(encode_url)
#
# decode_url = urllib.request.unquote(encode_url)
# print(decode_url)

# data = file.read()
# # dataline = file.readline()
#
# print(data)
# fhandle = open("1.html", "wb")
# fhandle.write(data)
# fhandle.close()


url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
file = urllib.request.urlopen(url)
print(file.getcode())

# 使用build_opener()修改报头
headers = ("User-Agent",
           "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fhandle = open('3.html', 'wb')
fhandle.write(data)
fhandle.close()

# 使用add_header()添加报头
req = urllib.request.Request(url)
req.add_header('User-Agent',
               "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
data = urllib.request.urlopen(req).read()
print(data)

# 设置超时
for i in range(1, 100):
    try:
        file = urllib.request.urlopen('http://yum.iqianyue.com', timeout=30)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->{}".format(e))





