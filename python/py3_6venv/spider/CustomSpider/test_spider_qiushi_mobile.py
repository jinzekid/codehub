# Author: Jason Lu
import re, time, random
import urllib.request

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
    # headers = ("User-Agent",
    #            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")

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
        pass

def getContent(proxy_addr, page_start, page_end):
    # 循环爬取各页的文章链接
    for page in range(page_start, page_end+1):
        str_url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
        print(str_url)
        data = use_proxy(proxy_addr, str_url)
        # data = urllib.request.urlopen(url).read().decode('utf-8')
        # print(data)
        # 可以正确解析
        pat_article = '<article class="item tiezi(.*?) class="username"(.*?)>(.*?)</a4>(.*?)<a4 href="/article/[0-9]{9}" class="text" (.*?)>(.*?)</a4>(.*?)'
        # pat_article = '<div class="article .*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>'

        list_article = re.compile(pat_article, re.S).findall(data)
        print(len(list_article))
        for article in list_article:
            # print(article)
            print("name:" + article[2].replace("\n",""))
            # print("用户:" + article[2])
            print("内容是:")
            content = article[5].replace("\n", "")
            print(content)
            print("\n")

        time.sleep(random.randint(0, 3))
    pass

proxy_addr = '223.85.96.238:8123'
# 不能翻页，解析的正则表达式也不一样
getContent(proxy_addr, 1, 1)


# def getcontent(url, page):
#     print(url)
#     # 模拟成游览器
#     # headers = ('User-Agent',
#     #            "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
#     headers = ("User-Agent",
#                "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36")
#     opener = urllib.request.build_opener()
#     opener.addheaders = [headers]
#     # 将opener安装为全局
#     urllib.request.install_opener(opener)
#     data = urllib.request.urlopen(url).read().decode('utf-8')
#     '''
#     以下正则表达式有问题
#     # print(data)
#     # 构建对应用户提取的正则表达式
#     # pat_user = 'target="_blank" title="(.*?)">'
#     pat_user = '<a4 href="/users/([0-9]{8})/" class="username" (.*?)>(.*?)</a4>'
#     # 寻找出所有的用户
#     list_user = re.compile(pat_user, re.S).findall(data)
#     # 构建段子内容提取的正则表达式
#     # pat_content = '<div class="content">(.*?)</div>'
#     pat_content = '<a4 href="/article/[0-9]{9}" class="text" (.*?)>(.*?)</a4>'
#     # 寻找出所有的内容
#     list_content = re.compile(pat_content, re.S).findall(data)
#     print(len(list_content))
#
#     # 通过for循环遍历段子内容
#     x = 1
#     for content in list_content:
#         content = content[1].replace("\n", "")
#         print(content)
#         print()
#         name = "content" + str(x)
#         exec(name + '=content')
#         x += 1
#
#     # 通过for循环遍历用户，输出该用户对应的内容
#     print(len(list_user))
#     y = 1
#     for user in list_user:
#         print(user[2])
#         name = "content" + str(y)
#         print("用户"+str(user[0])+"是:" + user[2])
#         print("内容是:")
#         exec("print("+name+")")
#         print("\n")
#         y+=1
#     '''
#
#     # 可以正确解析
#     pat_article = '<article class="item tiezi(.*?) class="username"(.*?)>(.*?)</a4>(.*?)<a4 href="/article/[0-9]{9}" class="text" (.*?)>(.*?)</a4>(.*?)'
#     list_article = re.compile(pat_article, re.S).findall(data)
#     print(len(list_article))
#     for article in list_article:
#         print("用户:" + article[2])
#         print("内容是:")
#         content = article[5].replace("\n", "")
#         print(content)
#         print("\n")
#
# # 分别获取各页的段子，通过for循环可以获取多页
# for i in range(1, 2):
#     url = "https://www.qiushibaike.com/8hr/page/"+str(i)+"/"
#     getcontent(url, i)