# Author: Jason Lu
import sys
import socket
import time
import gevent
from gevent import socket, monkey

HOST = "0.0.0.0"
monkey.patch_all()

def server(port):
    s = socket.socket()
    s.bind((HOST, port))
    s.listen(500)
    while True:
        cli, addr = s.accept()
        print("新链接来自 cli:", cli)
        gevent.spawn(handle_request, cli)


def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv:", data.decode())
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)

    except Exception as  ex:
        print(ex)
    finally:
        conn.close()


if __name__ == '__main__':
    server(8001)