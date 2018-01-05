# Author: Jason Lu
import socket, os, time

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
        data_recv = conn.recv(1024)

        if not data_recv:
            break

        print("执行指令: %s" %(data_recv.decode()))
        # conn.send(data_recv)

        str_cmd = data_recv.decode() # 转换字符串
        ret = os.popen(str_cmd).read()

        # 需要判断返回结果是否为空
        if len(ret) == 0:
            ret = "cmd has no output..."

        print("res: %s" %(ret))
        print("ret: %s" %(str(len(ret))))
        # 首先发送数据的长度
        len_ret = len(ret)
        conn.send(str(len_ret).encode("utf-8"))
        # time.sleep(0.5)

        # wait client to confirm
        client_ack = conn.recv(1024)
        print("%s" %(client_ack.decode()))
        # 然后发送整个数据
        conn.send(ret.encode("utf-8"))

    conn.close()

server.close()