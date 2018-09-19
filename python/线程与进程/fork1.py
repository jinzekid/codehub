# Author: Jason Lu
import os


def child():
    print('hello from child', os.getpid())
    os._exit(0) # 否则将回到父循环中

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent %s, child p:%s' % (os.getpid(), newpid))
        if input() == 'q': break

parent()