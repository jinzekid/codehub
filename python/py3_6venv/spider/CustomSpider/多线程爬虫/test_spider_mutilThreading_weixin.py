# Author: Jason Lu
import re, time, queue
import urllib.request
import urllib.error
import threading
from datetime import datetime


queue_url = queue.Queue()
listurl = []

# 创建全局默认的opener对象
def do_installGlobalOpener(proxy_addr):
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})

    # # 开启DebugLog
    # httphd = urllib.request.HTTPHandler(debuglevel=1)
    # opener = urllib.request.build_opener(proxy, httphd)

    # 创建一个自定义的opener对象
    opener = urllib.request.build_opener(proxy,
                                         urllib.request.HTTPHandler)
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

# 专门获取对应网址并处理为真实网址
class geturl(threading.Thread):
    def __init__(self, key, pagestart, pageend, proxy, urlqueue):
        threading.Thread.__init__(self)
        self.pagestart = pagestart
        self.pageend   = pageend
        self.proxy     = proxy
        self.urlqueue  = urlqueue
        self.key       = key

    def run(self):
        # page = self.pagestart
        str_keyword = urllib.request.quote(self.key)

        for page in range(self.pagestart, self.pageend+1):
            obj_date = datetime.today()
            timestamp = time.mktime(obj_date.timetuple())
            str_url = "http://weixin.sogou.com/weixinwap?type=2&page=" + str(page) + "&query=" + str_keyword + "&t=" + str(timestamp)
            print(str_url)
            data = use_proxy(self.proxy, str_url)
            print(data)
            # 可以正确解析
            pat_link = '<div class="list-txt">(.*?)<a href="(.*?)" (.*?)/a>'
            list_link = re.compile(pat_link, re.S).findall(data)
            print(len(list_link))
            for link in list_link:
                if link[1].startswith("http:"):
                    url = link[1].replace("amp;", "")
                    print(link[1].replace("amp;", ""))
                    # listurl.append(url)
                    # queue_url.put(url)
                    # queue_url.task_done()


class conrl(threading.Thread):
    def __init__(self, urlqueue):
        threading.Thread.__init__(self)
        self.queue_url = urlqueue

    def run(self):
        cnt = 1
        while(True):
            str_loading = "程序执行中....."
            pattern = '程序执行中(.{'+str(cnt)+'})'  # 前面有1位，后面有3位格式的字符(除了换行符以外任意字符)
            result1 = re.search(pattern, str_loading)
            print(str_loading)
            time.sleep(60)
            if self.queue_url.empty():
                print("程序执行完毕!")
                exit()

key = "人工智能"
proxy_addr = '111.155.124.85:8123'
t1 = geturl(key, 1, 2, proxy_addr, queue_url)
t1.start()

t2 = conrl(queue_url)
t2.start()




