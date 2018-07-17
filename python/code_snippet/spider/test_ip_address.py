g_ip_html = 'proxy_ip.html'

############################################################

"""
利用工厂模式，生成不同的header信息
"""


class HeaderFactory():
    def __init__(self):
        self.list_user_agent = [

        # For Android

        "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) \
        AppleWebKit/535.19 (KHTML, like Gecko) \
        Chrome/18.0.1025.166 Safari/535.19",
        "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) \
        AppleWebKit/534.30 (KHTML, like Gecko) \
        Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) \
        AppleWebKit/533.1 (KHTML, like Gecko) \
        Version/4.0 Mobile Safari/533.1",
        # For Firefox

        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) \
                Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Android; Mobile; rv:14.0) \
                Gecko/14.0 Firefox/14.0",
        # For chrome

        "Mozilla/5.0 (Windows NT 6.2; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/27.0.1453.94 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) \
        AppleWebKit/535.19 (KHTML, like Gecko) \
        Chrome/18.0.1025.133 Mobile Safari/535.19",
        # For iOS

        "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) \
        AppleWebKit/534.46 (KHTML, like Gecko) \
        Version/5.1 Mobile/9A334 Safari/7534.48.3",
        "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) \
        AppleWebKit/420.1 (KHTML, like Gecko) \
        Version/3.0 Mobile/3A101a Safari/419.3",

        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) \
        AppleWebKit/602.1.50 (KHTML, like Gecko) \
        CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"

        ]
        pass
    
    def get_random_user_agent(self):
        import random
        int_random = random.randint(0,len(self.list_user_agent)-1)
        return self.list_user_agent[int_random]

    """把方法当属性使用"""
    @property
    def header_info(self):
        header_default = [
            ("Accept", "text/html,application/xhtml+xml,\
                    application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"),
            ("Accept-Language", "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"),
            ("Connection", "keep-alive"),
            ("referer", ""),
            ("Accept-Encoding", "utf-8")
            ]
        header_default.append(('User-Agent', self.get_random_user_agent()))
        return header_default


############################################################

def get_ip_html():
    import urllib.request
    url = "http://www.xicidaili.com/wn/1"
    headers = ("User-Agent",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) \
                       AppleWebKit/602.1.50 (KHTML, like Gecko) \
                       CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read()

    fhandle = open(g_ip_html , 'wb')
    fhandle.write(data)
    fhandle.close()
    print('>>:finished save ip html....')

############################################################  

def parse_ip_html():
    print(">>:开始解析ip地址...")
    import pandas as pd
    with open(g_ip_html, 'r') as f:
        data = f.read()
        list_ip_address = bs4_paraser(data)

        data = pd.DataFrame(list_ip_address, columns=['ip','port','alive'])
        test_useful_ip_address(data.sort_values(by='alive' ,ascending=False))
        
        
############################################################    

def get_alive_minutes(alive):
    total_minutes = 0
    if alive.find('天') != -1:
        str_time = alive.replace('天', '')
        total_minutes = int(str_time)*24*60
    elif alive.find('小时') != -1:
        str_time = alive.replace('小时', '')
        total_minutes = int(str_time)*60
    else:
        str_time = alive.replace('分钟', '')
        total_minutes = int(str_time)
        
    return total_minutes


def bs4_paraser(html):
    from bs4 import BeautifulSoup
    import re
    all_values = []
    value = {}
    soup = BeautifulSoup(html, 'html.parser')
    
    # 获取影评的部分
    all_div = soup.find_all('tr')
    for row in all_div:
        dict_ip_info = {}
        all_td = row.find_all('td')
        
        if len(all_td) > 1:
            str_ip = re.findall(r"<td>(.+?)</td>",\
                    str(all_td[1]))[0]
            dict_ip_info['ip'] = str_ip
            
            str_port = re.findall(r"<td>(.+?)</td>",\
                    str(all_td[2]))[0]
            dict_ip_info['port'] = int(str_port)
            
            str_alive = re.findall(r"<td>(.+?)</td>",\
                    str(all_td[len(all_td)-2]))[0]
            dict_ip_info['alive'] = get_alive_minutes(str_alive)
            
            all_values.append(dict_ip_info)

    return all_values


# 测试IP地址是否有用
def test_useful_ip_address(df_ip):
    test_url = 'https://httpbin.org/anything/test_ip'
    import urllib.request
    import time
    for index, dict_ip_info in df_ip.iterrows():
        print(dict_ip_info['ip'])
        ip_address = dict_ip_info['ip']
        ip_port = dict_ip_info['port']

        proxy = urllib.request.ProxyHandler(\
                {'https': '%s:%s' %(ip_address, ip_port)\
                })
        # 是否开启DebugLog
        httphd = urllib.request.HTTPHandler(debuglevel=0)
        opener = urllib.request.build_opener(proxy, httphd)
        
        # 创建全局默认的opener对象
        urllib.request.install_opener(opener)
        
        # 使用添加报头
        req = urllib.request.Request(test_url)
        header_infos = HeaderFactory().header_info
        for info in header_infos:
            list_info = list(info)
            req.add_header(list_info[0], list_info[1])
        
        try:
            data = urllib.request.urlopen(req,timeout=6).read().decode('utf-8')
            if data is not None:
                print(data)
                print('good ip address:' + ip_address)
                print('================================')
        except Exception as e:
            print('请求超时...' + str(e))
      
        time.sleep(2)

#     proxy = urllib.request.ProxyHandler({'http': test_url})
#     # 是否开启DebugLog
#     httphd = urllib.request.HTTPHandler(debuglevel=0)
#     opener = urllib.request.build_opener(proxy, httphd)


'''############################################################'''

# get_ip_html()
parse_ip_html()
