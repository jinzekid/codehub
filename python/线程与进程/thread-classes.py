# Author: Jason Lu
"""
带有状态和run()行为的线程类示例，使用较高层面上的类java的
threading模块对象连接方法（而非mutexes或共享全局变量）在
主线程中探知线程结束时间
"""
import threading


class MyThread(threading.Thread):
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count # 各线程状态信息
        self.mutex = mutex # 共享对象，不是全局对象
        threading.Thread.__init__(self)

    def run(self): # run函数提供线程逻辑业务
        for i in range(self.count): # 仍然同步化stdout访问
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))

stdoutmutex = threading.Lock() # 与thread.allocate_lock()相同
threads = []

for i in range(10):
    thread = MyThread(i, 100, stdoutmutex)
    thread.start()
    threads.append(thread)

for thread in threads:
    #thread.start()
    thread.join() # 等待thread线程执行完成

print('Main thread exiting...')