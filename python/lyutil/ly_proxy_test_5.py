# Author: Jason Lu
def user_proxy(proxy_addr, url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


'''
test:w
182.100.238.129:4397
113.143.15.25:4368
119.116.157.118:4396
58.47.241.11:4368
113.231.83.153:4396
49.82.253.57:4364
123.189.140.168:4396
1.58.184.149:4332
180.119.140.146:4371
123.170.96.42:4372
'''

proxy_addr = "182.100.238.129:4397"
data = user_proxy(proxy_addr, "http://httpbin.org/get")
print(data)
print(len(data))
