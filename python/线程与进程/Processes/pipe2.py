# Author: Jason Lu
"""
和pipe1.py一样，不过将管道输入封装进stdio文件对象
在两个进程中逐行读取并关闭管道文件描述符
如果是ascii字节不麻烦
但是是中文就会遇到麻烦
"""

import os
import time


def chile(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('spam %03d\n' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5

def parent():
    pipein, pipeout = os.pipe() # 创建一个带有两个末端的管道
    if os.fork() == 0:          # 在子进程中想管道写入
        os.close(pipein)        # 在此关闭输入端
        chile(pipeout)
    else:                       # 在父进程中，监听管道
        os.close(pipeout)       # 在此关闭输出端
        pipein = os.fdopen(pipein) # 创建文本模式的输入文件对象
        while True:
            line = pipein.readline()[:-1] # 数据发送完之前保持阻塞
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


parent()