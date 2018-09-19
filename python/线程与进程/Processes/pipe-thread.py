# Author: Jason Lu
"""
匿名管道和线程而非进程，这个版本可以在windows上工作
"""

import os
import time
import threading

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5

def parent(pipein):
    while True:
        line = os.read(pipein, 32)
        print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)


