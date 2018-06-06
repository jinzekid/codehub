# Author: Jason Lu
'''
# b：类型只能接受ascii类型
# client.send(b"hello world!")
'''

'''
# 如果要传中文，需要encode("utf-8")
client.send("这是中文a".encode("utf-8"))
data = client.recv(1024)

print("recv: %s" %(data.decode()))
client.close()
'''

import socket

# 初始化socket
HOST = 'localhost'
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def do_main():
    while True:
        data_msg = input(">>:")

        if not data_msg:
            continue

        # 发送数据
        client.send(data_msg.encode("utf-8"))

        data_recv = client.recv(1024) # 等待返回的数据
        print("recv data:", data_recv.decode())


    client.close()


if __name__ == '__main__':
    do_main()