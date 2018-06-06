# Author: Jason Lu
# select多并发socket

import select
import socket
import queue

server = socket.socket()
server.bind(("0.0.0.0", 9000))
server.listen(1000)

# 设置成非阻塞模式
# 这样会，accept，recv不阻塞
server.setblocking(False)

inputs = [server, ] # 需要监测的链接
outputs = []
msg_dic = {}

while True:

    readable, writeable, exceptional = select.select(inputs, outputs, inputs )

    for r in readable:
        # 是否是server活动，代表来了一个新链接，
        # 建立连接
        if r is server:
            conn, addr = server.accept()
            print("来了一个新连接:", conn, addr)
            # 因为这个新建立的链接还没发数据过来，
            # 现在接受的话会报错，
            # 所以要想实现这个客户端发数据来时，server端能知道，
            # 就需要让select再监测这个conn
            inputs.append(conn)
            msg_dic[conn] = queue.Queue() # 初始化一个队列，后面存要返回给这个客户端的数据
        else:
            # 如果不是新连接，就是一个conn发送数据过来
            data = r.recv(1024)
            print(">>收到数据:", data.decode())
            msg_dic[r].put(data)

            outputs.append(r) # 放入返回的连接队列里

            # (r).send(data)

    # 要返回给客户端的连接列表
    for w in writeable:
        data = msg_dic[w].get()
        w.send(data) # 返回给客户端源数据

        # 删除数据
        outputs.remove(w) # 确保下次循环的时候writeable，不返回这个已经处理完的连接

    # 处理异常
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)

        inputs.remove(e)
        del msg_dic[e]



