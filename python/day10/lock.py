# Author: Jason Lu
# 虽然每个进程是独立的，但是屏幕是共享的

from multiprocessing import Process, Lock

def f(l, i):
    # 这个锁存在的意思在于屏幕打印
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(50):
        Process(target=f, args=(lock, num)).start()


