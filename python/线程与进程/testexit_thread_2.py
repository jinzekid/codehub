# Author: Jason Lu
"""
派生线程来观察共享全局内存的变化，线程通常在其运行的函数返回时退出，
但可以调用_thread.exit()结束其调用线程，_thread.exit和sys.exit相同，
也会抛出SystemExit一场，线程与可能被锁定的全局变量进行通行，小心；
在某些平台上可能需要做单元式的打印/输入调用---stdout是共享的
"""

import _thread as thread
import time
exitstat = 0
exit_mutexs = [False] * 5
thread_lock = thread.allocate_lock()

def child(i):
    global exitstat
    thread_lock.acquire()
    exitstat += 1   #为所有线程所共享
    threadid = thread.get_ident()
    print('Hello from child', threadid, exitstat, i)
    #thread.exit()
    thread_lock.release()
    exit_mutexs[i] = True
    print('never reached')

def parent():

    for i in range(5):
        thread.start_new_thread(child, (i, ))


    while False in exit_mutexs: pass

        #thread.start_new_thread(child, ())
        #if input() == 'q': break

    print('exit parent...')


if __name__ == '__main__': parent()
