# Author: Jason Lu
"""

分支进程基本操作，本程序启用了5个副本，与原有程序并行运行，
每个副本在同一个标准标准输出流上重复5次，分支操作复制进程
内存，包括文件描述符，目前分支操作在没有cygwin的windows下
不能进行，在windows下可以用os.spawnv或者mutilprocessing来替代，
spawnv大概相当于fork和exec的组合

这个程序有问题，因为运行到main process exiting后，子进程就结束了！奇怪。。。

"""

import os
import time


def counter(count):
    for i in range(count):
        #time.sleep(1)
        print('[%s] => %s' %(os.getpid(), i))

for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('Process %d spawned' % pid) # 在父进程中， 继续
    else:
        counter(5) # 否则在子/新的进程中进行
        os._exit(0) # 运行函数并推出


print('main process exiting.')