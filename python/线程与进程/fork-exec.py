# Author: Jason Lu
import os


parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid == 0:
        # 复制进程
        # 覆盖原来的程序
        # 不应该返回
        os.execlp('python', 'python', 'thread-count-wait1.py', str(parm))
        assert False, 'error starting progarm'
    else:
        print('Child id ', pid)
        if input() == 'q': break