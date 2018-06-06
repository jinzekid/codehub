# Author: Jason Lu

import socket, os

# 初始化socket
HOST = 'localhost'
PORT = 9999

server = socket.socket()
server.bind((HOST, PORT))
server.listen(500)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def do_main():
    print("等待客户端连接...")
    while True:
        # 等待客户端连接, 阻塞状态
        conn, addr = server.accept()
        print(">>连接来自:", conn)

        # 等待接受客户端数据
        while True:
            # 输入指令
            data_msg = conn.recv(1024)

            if not data_msg:
                break

            str_cmd = data_msg.decode()
            print(">>cmd:", str_cmd)
            res = os.popen(str_cmd).read()
            print(res)

            # 发送文件大小
            size_res = len(res)
            print("res size:", size_res)
            conn.send(str(size_res).encode("utf-8"))

            # 等待客户端的准备
            data_msg = conn.recv(1024)
            if int(data_msg) != 1:
                continue

            conn.send(res.encode("utf-8"))

        conn.close()

    server.close()

if __name__ == '__main__':
    do_main()