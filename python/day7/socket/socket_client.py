# Author: Jason Lu
# 客户端
'''
import socket

client = socket.socket() # 声明socket类型，同时生成socket连接对象
client.connect(('localhost', 6969))
'''
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
client = socket.socket() # 声明socket类型，同时生成socket连接对象
client.connect(('localhost', 6969))

# 改良版本
while True:
    msg = input(">>:").strip()

    # 不能send空
    if len(msg) == 0:
        continue

    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print("recv: %s" % (data.decode()))

client.close()
