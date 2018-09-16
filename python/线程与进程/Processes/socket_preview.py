# Author: Jason Lu
"""
套接字用于跨任务通信，启动线程，相互通过套接字通行，也适用于独立程序，因为套接字是系统级别的
类似FIFO，书中GUI和Internet更贴近时间套接字用例，
某些套接字服务器可能还需要与线程或进程中的客户端通行，
套接字传输字节字符串，后者可以是pickle后的对象或编码后的unicode文本
注意，如果线程中打印输输出可能重叠的话，则仍然需要同步化操作
"""
from socket import socket, AF_INET, SOCK_STREAM

port = 50008
host = 'localhost'

def server():
    sock = socket(AF_INET, SOCK_STREAM) # tcp连接ip地址
    sock.bind(('',port)) # 绑定到这台机器的端口上
    sock.listen(5) # 允许最多5个等待中的客户端
    while True:
        conn, addr = sock.accept() # 等待客户端连接
        data = conn.recv(1024) # 从这个客户端读取字节数据
        reply = 'server got: [%s]' % data
        conn.send(reply.encode()) # 将字节化的回复发回客户端

def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode()) # 向监听者发送字节数据
    reply = sock.recv(1024) # 从监听者哪里接受字节数据
    sock.close()
    print('client got: [%s]' % reply)


if __name__ == '__main__':
    from threading import Thread
    sthread = Thread(target=server)
    sthread.daemon = True   # 不等待服务器线程
    sthread.start()         # 等待子线程结束
    for i in range(5):
        Thread(target=client, args=('client%s' % i,)).start()
