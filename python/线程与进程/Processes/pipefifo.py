# Author: Jason Lu
"""
命名管道，os.mkfifo在windows下不能用（cygwin中可以），这里没有分支的必要
因为fifo文件管道对于进程为外部文件-父进程/子进程中共享文件描述符在这里没有效果
"""
import os
import time
import sys
fifoname = '/tmp/pipefifo' # 必须打开同名文件


def child():
    pipeout = os.open(fifoname, os.O_RDWR)
    # 作为文件描述符打开fifo

    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d \n' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5

        #如果换成input的话，不能及时的推送信息
        #msg = input()
        #size = os.write(pipeout, msg.encode())
        #print("str length: %d" % size)

def parent():
    pipein = open(fifoname, 'r') # 作为文本文件对象打开fifo
    while True:
        line = pipein.readline()[:-1] # 数据发送玩之前保持阻塞
        if line:
            print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time()))

if __name__ == "__main__":
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)
    if len(sys.argv) == 1:
        parent()
    else:
        child()





