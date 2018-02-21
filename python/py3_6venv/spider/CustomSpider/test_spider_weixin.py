# Author: Jason Lu
import re, time
import urllib.request
import urllib.error

# 创建全局默认的opener对象
def do_installGlobalOpener(proxy_addr):
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})

    # # 开启DebugLog
    httphd = urllib.request.HTTPHandler(debuglevel=1)
    opener = urllib.request.build_opener(proxy, httphd)

    # 创建一个自定义的opener对象
    # opener = urllib.request.build_opener(proxy,
    #                                      urllib.request.HTTPHandler)
    headers = ("User-Agent",
               "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 创建全局默认的opener对象
    urllib.request.install_opener(opener)

# 自定义函数，功能为使用代理服务器
def use_proxy(proxy_addr, url):
    try:
        import urllib.request
        # 创建全局默认的opener对象
        # 将opener安装为全局
        do_installGlobalOpener(proxy_addr)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.HTTPError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        # 若为URLError异常，延迟10s执行
        time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        # 若为Exception异常，延迟1s执行
        time.sleep(1)
    finally:
        # 延迟3s执行
        time.sleep(3)

def getWeixinLink(proxy_addr, keyword, page_start, page_end):
    str_keyword = urllib.request.quote(keyword)

    # 循环爬取各页的文章链接
    for page in range(page_start, page_end+1):
        str_url = "http://weixin.sogou.com/weixinwap?type=2&page=" + str(page) + "&query=" + str_keyword
        data = use_proxy(proxy_addr, str_url)
        # data = urllib.request.urlopen(url).read().decode('utf-8')
        print(data)
        # 可以正确解析
        pat_link = '<div class="list-txt">(.*?)<a href="(.*?)" (.*?)/a>'
        list_link = re.compile(pat_link, re.S).findall(data)
        print(len(list_link))
        for link in list_link:
            if link[1].startswith("http:"):
                print(link[1].replace("amp;", ""))
    pass


# str_keyword = input("请输入关键字-->:")
# page_start = int(input("起始页-->:"))
# page_end = int(input("结束页-->:"))


key = "物联网"
proxy_addr = '223.85.96.238:8123'
getWeixinLink(proxy_addr, key, 1, 2)


