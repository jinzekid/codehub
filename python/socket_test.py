# Author: Jason Lu

import socket
import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Failed to create socket. Error code: {_code}, Error message: {_message}".format(_code=str(msg[0]), __message=msg[1]))
    sys.exit()

print("Socket Created")

host = 'www.baidu.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

print("Ip address of {_host} is {_remote_ip}".format(_host=host, _remote_ip=remote_ip))

s.connect((remote_ip, port))

print("Socket Connected to {_host} on ip {_remote_ip}".format(_host=host, _remote_ip=remote_ip))


# 发送数据
message = "Get / Http/1.1\r\n\r\n"

try:
    s.sendall(message.encode())
except socket.error:
    print("Send failed")
    sys.exit()

print("Message send succesfully")

reply = s.recv(4096)

print(reply)

s.close()