# Author: Jason Lu
import telnetlib
import os


with open('download_4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # print(line)
        str_proxy_info = line.strip()
        protocol = 'HTTPS'
        # if protocol == 'HTTP' or protocol == 'HTTPS':
        ip, port = str_proxy_info.split(':')
        # print('%s   :    %s' % (ip, port))

        # 连接Telnet服务器
        try:
            tn = telnetlib.Telnet(ip, port=port, timeout=20)
        except:
            print('失败{}:{}'.format(ip, port))
        else:
            print('成功{}:{}'.format(ip, port))




