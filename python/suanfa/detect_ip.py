#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python

import uuid
def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

str_mac_address = get_mac_address()
print("本机的mac地址:" + str_mac_address)

#############################################################

import socket

myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
print("本机名字:" + myname)
print("本机ip地址:" + myaddr)

#############################################################

# 通过UDP获取本地ip
import socket

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s. getsockname()[0]
    finally:
        s.close()

    return ip

str_ip = get_host_ip()
print("通过UDP获取本地ip:" + str_ip)

#############################################################
from json import load
import urllib.request

my_ip = load(urllib.request.urlopen('http://httpbin.org/ip'))['origin']
print("网络外网ip地址:" + my_ip)





