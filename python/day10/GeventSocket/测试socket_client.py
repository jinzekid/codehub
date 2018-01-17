# Author: Jason Lu
import socket

HOST = "localhost"
PORT = 8001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input(">>:")
    client.send((msg.encode("utf-8")))

    data = client.recv(1024)
    print(data.decode())

client.close()