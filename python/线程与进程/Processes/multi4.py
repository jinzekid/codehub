# Author: Jason Lu
"""
可创建Process类的子类，就像threading.Thread一样；
Queue和queue.Queue的使用方法类似，不过它不是线程间的工具
而是进程间的工具
"""
import os
import time 
import queue

from multiprocessing import Process, Queue 
"""
进程安全的共享队列
队列是管道+锁/信号机
"""

class Counter(Process):
    label = ' @'
    def __init__(self, start, queue):
        self.state = start
        self.post = queue 
        Process.__init__(self)

    def run(self): # 新进程中调用start()时开始运行
        for i in range(3):
            time.sleep(1) # 模拟长时间运行任务
            self.state += 1
            print(self.label, self.pid, self.state) # self.pid为该子进程的pid
            self.post.put([self.pid, self.state]) # stdout文件为所有进程共享
        print(self.label, self.pid, '-')

if __name__ == '__main__':
    print('start', os.getpid())
    expected = 9

    post = Queue()
    p = Counter(0, post)
    q = Counter(100, post)
    r = Counter(1000, post)

    p.start(); q.start(); r.start()

    while expected:
        time.sleep(0.5)
        try:
            data = post.get(block=False)
        except queue.Empty:
            print('no data...')
        else:
            print('posted:', data)
            expected -= 1

    p.join(); q.join(); r.join()
    print('finish', os.getpid(), r.exitcode) 
