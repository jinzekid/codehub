# Author: Jason Lu

import socket

# 初始化socket
HOST = 'localhost'
PORT = 6969

client = socket.socket()
client.connect((HOST, PORT))

while True:

    data_recv = client.recv(1024)
    if not data_recv:
        continue
    # print("recv data:", data_recv.decode())

    data_msg = input(">>:")

    if not data_msg:
        continue

    client.send(data_msg.encode("utf-8"))

    data_recv = client.recv(1024)
    print("recv data:", data_recv.decode())

    client.close()