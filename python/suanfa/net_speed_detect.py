#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python

import urllib
from urllib import request
import urllib.request
import requests
from bs4 import BeautifulSoup
import time

#----------------------------------------------------------#

'''
    快速排序
        只能用于数值比较
'''
def quick_sort(array, str_key):
    if array is None:
        print("sort array can't be None!!")
        return None

    if len(array) < 2:
        return array
    else:
        pivot = int(array[0][str_key])
        # 所有小于基准值
        less = [device for device in array[1:] if int(device[str_key]) <= pivot]
        # 所有大于基准值
        greater = [device for device in array[1:] if int(device[str_key]) > pivot]
        return quick_sort(less, str_key) + [array[0]] + quick_sort(greater, str_key)

#----------------------------------------------------------#


str_router_url = 'http://192.168.3.1/'

req_header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/53/7.1m1',
  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  #'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
  'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding':'en-us',
  'Connection':'keep-alive',
  'Referer':str_router_url
             }

req_timeout = 5

from selenium import webdriver
url = str_router_url

driver = webdriver.Firefox()
driver.get(url)

# 等待一定时间，让js脚本加载完毕
driver.implicitly_wait(3)

#输入密码
password = driver.find_element_by_xpath('//*[@id="userpassword"]')
password.send_keys('kid1412ly')
#点击登陆
btn_submit = driver.find_element_by_xpath('//*[@id="loginbtn"]')
btn_submit.click()

print(">>> login... <<<")
print(">>> loading new page <<<")
while True:
    if str_router_url == driver.current_url:
        time.sleep(1)
        continue
    else:
        break

print("当前页面地址:" + driver.current_url)

driver.find_element_by_xpath('//*[@id="devicecontrol"]').click()

# 调出cookies
list_cookies = driver.get_cookies()
print("=======cookies信息=======")
print(list_cookies[0])
print(type(list_cookies[0]))
cookie = [item["name"] + "=" + item["value"] for item in list_cookies]
headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0",
                "Connection": "keep-alive",
                "referer": "http://192.168.3.1/html/content.html",
                "Accept-Encoding": "gzip, deflate"
               }
# 添加cookie值
headers['Cookie'] = cookie[0]
print("=============headers信息===============")
print(headers)

str_html_devices = 'http://192.168.3.1/html/devices.html'
driver.get(str_html_devices)

# 等待一定时间，让js脚本加载完毕
driver.implicitly_wait(3)

str_host_info = 'http://192.168.3.1/api/system/HostInfo'
import json
while True:
    req = request.Request(str_host_info, headers=headers, method='GET')
    response = request.urlopen(req).read().decode('utf-8')
    #print(type(response))
    #print(response)
    list_all_devices = list(json.loads(response))
    list_active_devices = []
    for device in list_all_devices:
        if device['Active'] == True:
            list_active_devices.append(device)

    print("=============联网设备===============")

    sorted_devices = quick_sort(list_active_devices, 'TxKBytes')
    for device in sorted_devices:
        print("联网设备名称:" + device['HostName'] + ", 接受速度:" + device['RxKBytes'] + ", 发送速度:" + device['TxKBytes'] )

    time.sleep(5)















