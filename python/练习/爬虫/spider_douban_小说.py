# Author: Jason Lu
#
#获取豆瓣读书信息
#

import urllib.request
import os
import re

str_keyword = '小说'
str_url_basic = 'https://book.douban.com/tag/'
patt = '<li class="subject-item">(.*?)</li>'


def fetch_html(url, keyword, cnt, type="T"):
    """
    :param url:
        基本url地址
    :param keyword:
        图书标签：比如，小说，外国文学，美国等
    :param cnt:
        获取数量，以20条为一页
    :param type:
        type=T：综合排序
        type=R：按出版日期排序
        type=S：按评价排序
    :return:
        返回的是一个字符串
    """

    encode_keyword = urllib.request.quote(keyword)
    url = url + encode_keyword + '?start='+str(cnt)+'&type='+type
    print('current %s' %url)
    # 使用build_opener()修改报头
    headers = ("User-Agent",
               "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read().decode('utf-8')

    # fhandle = open('douban_'+str_keyword+'_'+type+'_'+str(cnt)+'.html', 'wb')
    # fhandle.write(data)
    # fhandle.close()
    return data


def parse_html_data(file_data):
    data = file_data
    result = re.compile(patt, re.S).findall(data)
    print(len(result))
    for book in result:
        book_info = re.compile('<div class="info">(.*?)<div class="pub">', re.S) \
            .findall(book)
        book_info_title = re.compile('title="(.*?)"', re.S).findall(
            book_info[0])
        print(book_info_title[0])
        print()

def parse_html_file(file_name):

    with open(file_name, 'rb') as f:
        data = f.read().decode('utf-8')
        result = re.compile(patt, re.S).findall(data)
        print(len(result))
        for book in result:
            book_info = re.compile('<div class="info">(.*?)<div class="pub">', re.S)\
                          .findall(book)
            book_info_title = re.compile('title="(.*?)"', re.S).findall(
                book_info[0])
            print(book_info_title[0])
            print()
    pass

parse_html_data(fetch_html(str_url_basic, str_keyword, "T", 20))



