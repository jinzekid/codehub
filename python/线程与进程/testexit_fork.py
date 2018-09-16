# Author: Jason Lu
"""
分支子进程，用os.wait观察其退出状态，分支在unix和cygwin下能够进行
但是windows python3.1标准版中不能，请注意，派生线程共享全局变量，
但每个分支进程拥有其自己的全局变量副本（分支共享文件描述符）
exitstat在这里将保持不变，而如果是线程的话将发生变化
"""


import os
exitstat = 0

def child():
    global exitstat # 更改这个进程的全局变量
    exitstat += 1   # 发送到父进程的wait函数的退出状态
    print('Hello from child', os.getpid(), exitstat)
    os._exit(exitstat)
    print('never reached')

def parent():
    while True:
        newpid = os.fork()  # 开始进程的新副本
        if newpid == 0: # 如果是在副本中，那么运行子进程的逻辑业务
            child() # 持续循环，知道控制台输入'q'
        else:
            pid, status = os.wait()
            print('Parent got ', pid, status, (status >> 8))
            if input() == 'q': break

if __name__ == '__main__': parent()
