# Author: Jason Lu

import socket

# 初始化socket
HOST = 'localhost'
PORT = 9999

server = socket.socket()
server.bind((HOST, PORT))
server.listen(100)


def do_main():
    print("开始启动监听...")
    while True:
        # 等待接受socket连接
        conn, addr = server.accept()
        print(">>来自连接:", conn)

        while True:

            data_recv = conn.recv(1024)
            if not data_recv:
                break

            if data_recv.decode() == "":
                print("client已经断开...222")
                break

            print("recv data:", data_recv.decode())
            conn.send(data_recv)

        conn.close()

    server.close()


if __name__ == '__main__':
    do_main()
