# Author: Jason Lu
import re, time, random

from lyutil.ly_ProxyRequestUtil import proxyrequest

def getContent(page_start, page_end):
    # 循环爬取各页的文章链接
    for page in range(page_start, page_end+1):
        str_url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
        print(str_url)
        data = proxyrequest(str_url).getdata()#use_proxy(proxy_addr, str_url)
        # data = urllib.request.urlopen(url).read().decode('utf-8')
        # print(data)
        # 可以正确解析
        # pat_article = '<article class="item tiezi(.*?) class="username"(.*?)>(.*?)</a4>(.*?)<a4 href="/article/[0-9]{9}" class="text" (.*?)>(.*?)</a4>(.*?)'
        pat_article = '<div class="article .*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>'

        list_article = re.compile(pat_article, re.S).findall(data)
        print(len(list_article))
        for article in list_article:
            # print(article)
            print("name:" + article[0].replace("\n",""))
            # print("用户:" + article[2])
            print("内容是:")
            content = article[1].replace("\n", "")
            print(content)
            print("\n")

        time.sleep(random.randint(0, 3))
    pass

getContent(1, 3)