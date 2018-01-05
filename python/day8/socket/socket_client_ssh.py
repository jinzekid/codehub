# Author: Jason Lu

import socket

client = socket.socket() # 声明socket类型，同时生成socket连接对象

client.connect(('localhost', 8080))
print("client socket connect success...")
bool_successOpen = True

if bool_successOpen:
    while True:
        data = input(">>:").strip()

        if len(data) == 0:
            continue

        print("发送的命令: %s" %(data.encode("utf-8")))
        client.send(data.encode("utf-8"))

        # 首先接受命令结果的长度
        size_totalData = client.recv(1024)
        print("命令结果大小: %s" %(size_totalData.decode()))

        recv_size = 0
        recv_data = b''
        recv_totalSize = int(size_totalData.decode())
        print("totalsize=%s" %(recv_totalSize))

        client.send("准备好接受数据了...".encode("utf-8"))

        while recv_size < recv_totalSize:
            data = client.recv(1024)
            recv_size += len(data)
            recv_data += data
            print("当前收到数据大小：%s" %(recv_size))
            print("当前收到数据: %s" % (data.decode()))
        else:
            print("recv done...一共收到数据: %s" %(recv_size))
            print("======recv data======")
            print("%s" %(recv_data))

    client.close()

