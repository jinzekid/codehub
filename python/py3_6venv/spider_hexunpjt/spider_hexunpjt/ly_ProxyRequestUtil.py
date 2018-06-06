# Author: Jason Lu
import re, time, random
import urllib.request

# proxies = {'http':'http://10.10.10.10:8765',
#            'https':'https://10.10.10.10:8765',
#            'http':'http://223.85.96.238:8123'}

# headers = ("User-Agent",
        #            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36")
# headers = ("User-Agent",
#            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")


header_useragents = [{"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X "
                                    "10_13_0) AppleWebKit/537.36 (KHTML, "
                                    "like Gecko) Chrome/64.0.3282.167 Safari/537.36"},
                     {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"},
                     {"User-Agent":"Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0"}]


header_default = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
                "Connection": "keep-alive",
                "referer": "",
                "Accept-Encoding": "utf-8"
               }


'''常用user-agent

1.Android

Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
2.Firefox

Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0
Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0
3.Google Chrome

Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36
Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19
4.iOS

Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3
Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3

'''


class proxyutil(object):

    def __init__(self, f_proxy=None):
        print(">>>初始化代理地址<<<")
        self.f_proxy = f_proxy
        self.list_proxy = []
        self.int_index = 0
        pass

    def parse_httpProxy(self):
        if self.f_proxy is None:
            print(">>>解析文件不存在<<<")
            return

        print(">>>开始解析http代理地址<<<")
        with open(self.f_proxy, 'r', encoding='utf-8') as f:
            for line in f:
                str_proxy_info = line.strip()
                ip, port = str_proxy_info.split(':')

                dict_httpproxy = {"http": '%s:%s' % (ip, port)}
                self.list_proxy.append(dict_httpproxy)

        print(">>>获取文件中所有http代理地址列表<<<")
        print(self.list_proxy)
        print(">>>>>>>>>>>>>>>>>>>>>>>>")
        return self

    def get_proxyLen(self):
        return len(self.list_proxy)


    def parse_httpsProxy(self):
        pass


    def get_nextProxyInfo(self, index=-1):
        print(">>>获取一个http代理地址<<<")
        _len_proxy = len(self.list_proxy)
        _obj_proxyInfo = None
        if index != -1 and index < _len_proxy:
            self.int_index = (index + 1) % _len_proxy
            _obj_proxyInfo = self.list_proxy[self.int_index]
        else:
            self.int_index = (self.int_index + 1) % _len_proxy
            _obj_proxyInfo = self.list_proxy[self.int_index]

        if _obj_proxyInfo is not None:
            print(">>>%s<<<" %_obj_proxyInfo)
        return _obj_proxyInfo

    def __repr__(self):
        print(self.list_proxy)

class proxyconfig(object):

    def __init__(self, proxy=None, headers=header_default, saveCookie=False):
        print(">>>配置代理设置<<<")
        self.b_saveCookie = saveCookie
        self.headers = headers
        self.proxy = proxy
        pass

    def update_header(self):
        pass


    # 创建全局默认的opener对象
    def install_globalOpener(self, b_openDebug=False):
        # proxy = urllib.request.ProxyHandler({'http': self.proxy_addr})
        if self.proxy is None:
            print(">>>设置没有代理地址opener<<<")
            opener = urllib.request.build_opener(urllib.request.HTTPHandler)
        else:
            print(">>>开始设置opener, 代理地址:%s<<<" %self.proxy)
            proxy_support = urllib.request.ProxyHandler(self.proxy)
            # 创建一个自定义的opener对象
            # 开启DebugLog
            if b_openDebug:
                print(">>>设置调试模式<<<")
                httphd = urllib.request.HTTPHandler(debuglevel=1)
                opener = urllib.request.build_opener(proxy_support, httphd)
            else:
                opener = urllib.request.build_opener(proxy_support,
                                                     urllib.request.HTTPHandler)

        if self.b_saveCookie:
            print(">>>设置cookie模式<<<")
            # 希望登录状态一直保持，使用Cookie处理
            import http.cookiejar
            # 使用http.cookiejar.CookieJar()创建CookieJar对象
            cjar = http.cookiejar.CookieJar()
            # 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
            opener.add_handler(urllib.request.HTTPCookieProcessor(cjar))


        # 建立空列表，为了指定格式存储头信息
        if self.headers is not None:
            print(">>>设置header信息<<<")
            headall = []
            for key, value in self.headers.items():
                item = (key, value)
                headall.append(item)

            print("%s" %headall)
            # 指定格式的headers信息添加好
            opener.addheaders = headall

        # 创建全局默认的opener对象
        print(">>>创建全局默认的opener对象<<<")
        urllib.request.install_opener(opener)


class proxyrequest(object):

    def __init__(self, url,
                 putil=None,
                 pconfig=None,
                 openDebug=False):
        self.url        = url
        self.putil = putil
        self.pconfig = pconfig

    # 自定义函数，功能为使用代理服务器
    def get_data(self, b_decoded=True):
        try:
            # 创建全局默认的opener对象
            # 将opener安装为全局
            # self.do_installGlobalOpener(b_saveCookie=self.savecookie, b_openDebug=self.opendebug)

            if b_decoded:
                data = urllib.request.urlopen(self.url).read().decode('utf-8')
            else:
                data = urllib.request.urlopen(self.url).read()

            return data
        except urllib.error.HTTPError as e:
            print(">>>发生了HTTPError异常<<<")
            if hasattr(e, 'code'):
                print(e.code)
            if hasattr(e, 'reason'):
                print(e.reason)
        except urllib.error.URLError as e:
            print(">>>发生了URLError异常<<<")
            if hasattr(e, 'code'):
                print(e.code)
            if hasattr(e, 'reason'):
                print(e.reason)
            # 若为URLError异常，延迟10s执行
            time.sleep(10)
        except Exception as e:
            print(">>>发生了其他异常<<<")
            print("exception:" + str(e))
            # 若为Exception异常，延迟1s执行
            time.sleep(1)
        finally:
            # 延迟3s执行
            time.sleep(1)
            pass






'''
from urllib.parse import urlencode
params = {
    'name':'gemeny',
    'age':12
}
base_url = 'http://www.baidu.com'
url = base_url + urlencode(params)
print(url)
'''
