# Author: Jason Lu
def use_proxy(proxy_addr, url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})

    # 开启DebugLog
    httphd = urllib.request.HTTPHandler(debuglevel=1)
    opener = urllib.request.build_opener(proxy, httphd)


    # 创建一个自定义的opener对象
    # opener = urllib.request.build_opener(proxy,
    #                                      urllib.request.HTTPHandler)
    # 创建全局默认的opener对象
    urllib.request.install_opener(opener)

    # 使用add_header()添加报头
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
    data = urllib.request.urlopen(req).read().decode('utf-8')
    # data = urllib.request.urlopen(url).read().decode('utf-8')
    return data

proxy_addr = '61.135.217.7:80'
data = use_proxy(proxy_addr, "http://www.baidu.com")
print(len(data))
print(data)








