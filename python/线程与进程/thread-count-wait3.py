# Author: Jason Lu
"""
传入所有线程共享的mutex对象而非所有全局对象，和上下文管理器
语句一起使用，实现锁的自动获取/释放，添加休眠功能的调用以
避免繁忙的循环并模拟真是工作
"""
import _thread as thread, time


stdoutmutex = thread.allocate_lock()
numthreads = 5
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]


def counter(myId, count, mutex): # 传入共享对象
    for i in range(count):
        time.sleep(1 / ( myId+1 ))
        with mutex: #自动获取/释放锁，with语句
            print('[%s] => %s' %(myId, i))

    exitmutexes[myId].acquire() # 全局层次，向主线程发送信号


for i in range(numthreads):
    thread.start_new_thread(counter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes): time.sleep(0.25)

print('main thread exiting.')