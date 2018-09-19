# Author: Jason Lu
"""
匿名管道的基本操作，
父进程在同一时间内结束从管道中读取两条消息，子进程写入两条不同的消息
不过在某些平台或者某些配置下它们可能混在一起，或处理时间接近到
被父进程作为同一个操作的结果锁读取。
示例：
Parent 4288 got [b'Spam 004Spam 000'] at 1533766278.7299242
实际上，父进程不管管道的另一端，只是请求读取，每次最多32字节，
管道 中有数据时将其读取，不管数据本身是什么
"""
import os
import time


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz) # 让父进程等待
        msg = ('Spam %03d, child id: %s' % (zzz, os.getpid())).encode()  #
        # 管道是二进制字节
        os.write(pipeout, msg) # 发送到父进程
        zzz = (zzz + 1) % 5 # 4后进到0

def parent():
    pipein, pipeout = os.pipe() # 创建带有两个末端的管道

    if os.fork() == 0:  # 复制此进程
        child(pipeout)  # 在副本中运行child
    else:               # 在父进程中，监听管道
        while True:
            line = os.read(pipein, 32)  # 数据发送完之前保持阻塞
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))

parent()