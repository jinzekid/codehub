# Author: Jason Lu
"""
使用多进程匿名管道进行通信，返回两个connection对象来分别代表管道的两端
对象从一段发送，在另一端接受，不过管道默认是双向的
"""

import os
import sys
import time
from multiprocessing import Process, Pipe

def sender(pipe):
    """在匿名管道上向父进程发送对象"""
    """
    pipe.send(['spam'] + [42, 'eggs'])
    pipe.close()
    """
    """
    zzz = 0
    while True:
        time.sleep(zzz)
        pipe.send(['spam'] + [42, 'eggs'])
        zzz = (zzz + 1) % 3
    """
    while True:
        input("请输入:")
        pipe.send(['spam'] + [42, 'eggs'])
        #pipe.send(msg.encode())

def talker(pipe):
    """通过管道发送和接受对象"""
    pipe.send(dict(name='Bob', spam=42))
    while True:
        reply = pipe.recv()
        print('talker got:' , reply)



def speaker(pipe):
    while True:
        msg = input(">>:")
        reply = pipe.send(msg)
        print('speaker got:' , reply)


if __name__ == '__main__':
    """
    (parentEnd, childEnd) = Pipe()
    Process(target=sender, args=(childEnd, )).start() # 派生带有管道的子进程
    print('111parent got:', parentEnd.recv())            # 从子进程处接受
    parentEnd.close()                                 # 或者在全局目录中自动关闭
    """
    """
    (parentEnd, childEnd) = Pipe()
    child = Process(target=talker, args=(childEnd,))
    child.start()
    print('222parent got:' , parentEnd.recv())           # 从子进程处接受
    parentEnd.send({x * 2 for x in 'spam'})           # 向子进程发送
    child.join()                                      # 等待子进程退出
    print('parent exit')
    """
    """
    (parentEnd, childEnd) = Pipe()
    Process(target=sender, args=(childEnd, )).start()
    while True:
        try:
            #msg = parentEnd.recv()
            print('111parent got:')
        except EOFError as e:
            print("except e:%s" % e)    
             
    """

    (parentEnd, childEnd) = Pipe()
    arg = sys.argv[1]
    if arg == 'child':
        Process(target=talker, args=(childEnd,)).start()
    else:
        speaker(parentEnd)

