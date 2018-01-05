# Author: Jason Lu

import socket, os
import hashlib

def do_checkFileMd5(str_filename, str_origin_md5):
    # 准备md5
    m = hashlib.md5()
    # 4.打开文件
    with open(str_filename, "r", encoding="utf-8") as f_config:
        # 循环查找字符串
        for line in f_config:
            m.update(line.encode("utf-8"))

    if m.hexdigest() == str_origin_md5:
        print("文件传输正确...")
        return True

    return False


client = socket.socket() # 声明socket类型，同时生成socket连接对象

client.connect(('localhost', 8080))
print("client socket connect success...")
bool_successOpen = True

if bool_successOpen:
    while True:
        str_filename = input(">>:").strip()

        if len(str_filename) == 0:
            continue

        print("发送的命令: %s" %(str_filename.encode("utf-8")))
        client.send(str_filename.encode("utf-8"))

        ret = client.recv(1024)
        if int(ret.decode()) == -1:
            print("文件不存在，请重新输入文件名!")
            continue

        # 首先接受命令结果的长度
        size_totalData = ret
        print("文件大小: %s" %(size_totalData.decode()))

        info = '''客户端已经准备接受文件: %s 数据大小: %s''' %(str_filename, size_totalData)
        client.send(info.encode("utf-8"))

        recv_size = 0
        recv_data = b''
        recv_totalSize = int(size_totalData.decode())
        print("totalsize=%s" %(recv_totalSize))

        str_filename_bak = '''%s.bak''' %(str_filename)
        f_new = open(str_filename_bak, "w", encoding="utf-8")
        while recv_size < recv_totalSize:
            data = client.recv(1024)
            recv_size += len(data)
            recv_data += data
            f_new.write(data.decode())
            print("当前收到数据大小：%s" %(recv_size))
            print("当前收到数据: %s" % (data.decode()))
        else:
            print("recv done...一共收到数据: %s" %(recv_size))
            print("======recv data======")
            print("%s" %(recv_data))
            f_new.close()
            print("文件写入成功...")
            info = '''2'''
            client.send(info.encode("utf-8"))

        # 接受md5数据
        ret = client.recv(1024)
        do_checkFileMd5(str_filename_bak, ret.decode())

    client.close()


