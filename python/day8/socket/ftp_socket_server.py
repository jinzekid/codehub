# Author: Jason Lu
# 1.读取文件名
# 2.检测文件是否存在
# 3.打开文件
# 4.检测文件大小
# 5.发送文件大小
# 6.等待客户端确认
# 7.开始边读边发送文件
# 8.最后发一个完整的md5确认

import socket
import os
import time
import hashlib

# 初始化socket
server = socket.socket()
server.bind(("localhost", 8080))
server.listen(5)

# 开始等待接受连接
while True:
    print("等待连接...")
    conn, addr = server.accept()
    print("有连接来自: %s %s" %(conn, addr))

    while True:
        # 1.读取文件名
        data_recv = conn.recv(1024)

        if not data_recv:
            break

        print("读取文件名: %s" %(data_recv.decode()))
        str_filename = data_recv.decode()

        # 2.检测文件是否存在
        if os.path.exists(str_filename) == False:
            print("File doesn't exist...")
            conn.send(str(-1).encode("utf-8"))
            continue

        # 3.获取文件大小
        fsize = os.path.getsize(str_filename)
        conn.send(str(fsize).encode("utf-8"))

        # wait client to confirm
        client_ack = conn.recv(1024)
        print("%s" %(client_ack.decode()))
        print("服务器端准备开始发送文件...")

        # 准备md5
        m = hashlib.md5()
        # 4.打开文件
        with open(str_filename, "r", encoding="utf-8") as f_config:
            # 循环查找字符串
            for line in f_config:
                m.update(line.encode("utf-8"))
                conn.send(line.encode("utf-8"))

        print("file md5: %s" %(m.hexdigest()))

        # wait client to confirm
        client_ack = conn.recv(1024)
        if int(client_ack) == 2:
            print("发送md5校验码...")
            # 5.发送md5数据进行校验
            conn.send(m.hexdigest().encode("utf-8"))

    conn.close()

server.close()


