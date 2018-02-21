# Author: Jason Lu
import re, time, random
import urllib.request

proxies = {'http':'http://10.10.10.10:8765','https':'https://10.10.10.10:8765', 'http':'http://223.85.96.238:8123'}

class proxyrequest(object):

    def __init__(self, url):
        self.url        = url

    # 创建全局默认的opener对象
    def do_installGlobalOpener(self):
        # proxy = urllib.request.ProxyHandler({'http': self.proxy_addr})
        proxy_support = urllib.request.ProxyHandler(proxies)

        # # 开启DebugLog
        # httphd = urllib.request.HTTPHandler(debuglevel=1)
        # opener = urllib.request.build_opener(proxy, httphd)

        # 创建一个自定义的opener对象
        opener = urllib.request.build_opener(proxy_support,
                                             urllib.request.HTTPHandler)
        # headers = ("User-Agent",
        #            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36")
        headers = ("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")

        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        # 创建全局默认的opener对象
        urllib.request.install_opener(opener)

    # 自定义函数，功能为使用代理服务器
    def getdata(self):
        try:
            import urllib.request
            # 创建全局默认的opener对象
            # 将opener安装为全局
            self.do_installGlobalOpener()
            data = urllib.request.urlopen(self.url).read().decode('utf-8')
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