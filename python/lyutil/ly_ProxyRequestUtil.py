# Author: Jason Lu
import re, time, random
import urllib.request

proxies = {'http':'http://10.10.10.10:8765',
           'https':'https://10.10.10.10:8765',
           'http':'http://223.85.96.238:8123'}

# headers = ("User-Agent",
        #            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36")
headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")


class proxyrequest(object):

    def __init__(self, url, proxy=proxies, header=headers, saveCookie=False, openDebug=False):
        self.url        = url
        self.savecookie = saveCookie
        self.opendebug  = openDebug
        self.proxy = proxy
        self.header = header

    # 创建全局默认的opener对象
    def do_installGlobalOpener(self, b_saveCookie=False, b_openDebug=False):
        # proxy = urllib.request.ProxyHandler({'http': self.proxy_addr})
        proxy_support = urllib.request.ProxyHandler(proxies)

        # 创建一个自定义的opener对象
        # 开启DebugLog
        if b_openDebug:
            httphd = urllib.request.HTTPHandler(debuglevel=1)
            opener = urllib.request.build_opener(proxy_support, httphd)
        else:
            opener = urllib.request.build_opener(proxy_support,
                                                 urllib.request.HTTPHandler)

        if b_saveCookie:
            # 希望登录状态一直保持，使用Cookie处理
            import http.cookiejar
            # 使用http.cookiejar.CookieJar()创建CookieJar对象
            cjar = http.cookiejar.CookieJar()
            # 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
            opener.add_handler(urllib.request.HTTPCookieProcessor(cjar))



        opener = urllib.request.build_opener()

        # 建立空列表，为了指定格式存储头信息
        headall = []
        for key, value in self.header.items():
            item=(key, value)
            headall.append(item)

        # 指定格式的headers信息添加好
        opener.addheaders = headall

        # 创建全局默认的opener对象
        urllib.request.install_opener(opener)

    # 自定义函数，功能为使用代理服务器
    def getdata(self, b_decoded=True):
        try:
            # 创建全局默认的opener对象
            # 将opener安装为全局
            self.do_installGlobalOpener(b_saveCookie=self.savecookie, b_openDebug=self.opendebug)
            if b_decoded:
                data = urllib.request.urlopen(self.url).read().decode('utf-8')
            else:
                data = urllib.request.urlopen(self.url).read()

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
            pass