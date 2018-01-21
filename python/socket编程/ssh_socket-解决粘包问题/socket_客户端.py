# Author: Jason Lu

import socket

# 初始化socket
HOST = 'localhost'
PORT = 9999
SIZE = 100

client = socket.socket()
client.connect((HOST, PORT))
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def do_main():

    while True:
        data_msg = input(">>:")

        if not data_msg:
            continue

        # 发送数据，比如命令，希望服务端返回大数据
        client.send(data_msg.encode("utf-8"))

        # 如果数据大于设置的接受大小
        # 需要不断的接受数据
        # 首先需要接受数据的大小
        data_recv_size = client.recv(1024)

        size_totalSize = int(data_recv_size.decode())
        size_recved = 0
        size_toRecv = 1024
        data_recv = b''

        # 准备接受服务端数据
        client.send("1".encode("utf-8"))
        while True:
            # 如果数据接受完成
            if size_recved >= size_totalSize:
                break
            # 说明最后一段数据，小于size_toRecv
            if size_totalSize - size_recved < size_toRecv:
                size_toRecv = size_totalSize - size_recved

            data_recv += client.recv(size_toRecv)
            size_recved += size_toRecv
            print("Recv size:%s" % (size_recved))

        print(data_recv.decode())
        print("total size: %s, recv size:%s" %(size_totalSize, size_recved))

    client.close()

if __name__ == '__main__':
    do_main()