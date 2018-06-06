# Author: Jason Lu

import threading
import time

# 一般调用
'''
def run(n):
    print("task:", n)
    time.sleep(2)


t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2",))

t1.start()
t2.start()
'''

# 继承调用
'''
class MyThread(threading.Thread):

    def __init__(self, n):
        super(MyThread, self).__init__() # 新式类写法
        self.n = n

    # 类的必须是run方法
    def run(self):
        print("running task:", self.n)


t1 = MyThread("t1")
t2 = MyThread("t2")

t1.start()
# t1.join() # 等待线程t1执行完
t2.start()
'''

'''
# 主线程启动后，子线程是并行的。
def run(n):
    print("task:", n)
    time.sleep(2)
    print("task %s done" %(n))

start_time = time.time()
list_threads = []
for i in range(5):
    t = threading.Thread(target=run, args=("t-%s" %i ,))
    t.start()
    list_threads.append(t)

print("-----current active threads----- %s" %(threading.active_count()))


for thread in list_threads:
    thread.join()


print("-----current active threads----- %s" %(threading.active_count()))
print("-----all threads finished----- %s" %(threading.current_thread()))

print("cost: %s" %(time.time() - start_time))
'''

# 守护线程实例
'''
def run(n):
    print("task:", n)
    time.sleep(2)
    print("task %s done" %(n))

start_time = time.time()
list_threads = []
for i in range(5):
    t = threading.Thread(target=run, args=("t-%s" %i ,))
    t.setDaemon(True) # 把当前线程设置为守护线程, 一定要在start之前
    t.start()
    list_threads.append(t)

print("-----current active threads----- %s" %(threading.active_count()))
print("-----all threads finished----- %s" %(threading.current_thread()))
print("cost: %s" %(time.time() - start_time))
'''

# 先生成锁的实例
lock = threading.Lock()

num = 0
start_time = time.time()
list_threads = []

def run(n):
    lock.acquire()
    global num
    num += 1
    time.sleep(1)
    lock.release()

for i in range(5):
    t = threading.Thread(target=run, args=("t-%s" %i ,))
    t.start()
    list_threads.append(t)

for thread in list_threads:
    thread.join()

print("-----current active threads----- %s" %(threading.active_count()))
print("-----all threads finished----- %s" %(threading.current_thread()))

print("num:", num)



