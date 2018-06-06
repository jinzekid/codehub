# Author: Jason Lu

'''
import socket

server = socket.socket()
server.bind(('localhost', 6969)) #绑定监听端口
server.listen(5) #监听数量5个
'''
'''
print("开始等电话了...")
conn, addr = server.accept() # 等电话打进来
print("电话来了...%s" %(conn))
'''

# 英文
'''
data = conn.recv(1024)
print("recv: %s" % (data))
'''
# 中文
''''
data = conn.recv(1024)
print("recv: %s" % (data.decode()))

conn.send(data.upper())
'''

# 改良版本
import os
import socket

server = socket.socket()
server.bind(('localhost', 6969)) #绑定监听端口
server.listen(5) #监听数量5个

while True:
    print("开始等电话了...")
    conn, addr = server.accept()  # 等电话打进来
    print("电话来了,...来自: %s" %(conn))

    while True:
        data = conn.recv(1024)

        if not data:
            print("client已经断开...111")
            break

        if data.decode() == "":
            print("client已经断开...222")
            break

        print("recv: %s" % (data.decode()))
        #conn.send(data.upper())

        # 执行命令(通过client发送的命令来执行对应的命令)
        '''
        str_cmd = data.decode() # 转换字符串
        res = os.popen(str_cmd).read()
        conn.send(res.encode("utf-8"))
        '''

        # 如果发送发文件，比如视频文件


    conn.close()

server.close()


