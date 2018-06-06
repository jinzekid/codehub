# Author: Jason Lu
import threading
class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(10):
            print("我是线程A...."+ str(i))

class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(10):
            print("我是线程B...."+ str(i))


t1 = A()
t2 = B()
t1.start()
t2.start()







