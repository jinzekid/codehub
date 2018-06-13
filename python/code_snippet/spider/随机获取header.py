#!/Users/jasonlu/.virtualenvs/pyven3_6/bin/python 

list_user_agent = [
        # For Android
        "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
        "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # For Firefox
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0",
        # For chrome 
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",
        # For iOS
        "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
        "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3",

        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
        ]

def get_random_user_agent(list_user_agent):
    """
    随机生成一个User-Agent信息
    """
    import random 
    int_random = random.randint(0,len(list_user_agent)-1)
    return list_user_agent[int_random]


def get_header_info():
    """
    返回自定header信息
    """
    header_default = [
            ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"),
            ("Accept-Language", "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"),
            ("Connection", "keep-alive"),
            ("referer", ""),
            ("Accept-Encoding", "utf-8")
            ]
    header_default.append(('User-Agent', get_random_user_agent(list_user_agent)))
    return header_default


def get_data(url, header_info=None, post_data = None, proxy_addr = None):
    import urllib.request
    import urllib.parse 

    opener = urllib.request.build_opener()
    opener.addheaders = header_info
    post_data_encoded = urllib.parse.urlencode(post_data).encode('utf-8')

    data = opener.open(url, data=post_data_encoded).read()

    #req = urllib.request.Request(url, post_data_encoded)
    #data = urllib.request.urlopen(req).read()
    return data

data = get_data(url="http://httpbin.org/post", header_info=get_header_info(), post_data={'name':'lu'})
print(data.decode('utf-8'))
print(len(data))




