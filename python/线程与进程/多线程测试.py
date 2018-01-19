# Author: Jason Lu
import threading, time
# 一般方法
# def run(n):
#     print("running task:", n)
#     time.sleep(2)
#     print("task %s done" %(n))
#     pass
#
# def do_main():
#     for i in range(5):
#         t = threading.Thread(target=run, args=(i, ))
#         t.start()
#
# if __name__ == '__main__':
#     do_main()

# 继承方法
class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__() #新式类继承方法
        self.n = n
        pass

    def run(self):
        print("running task:", self.n)
        time.sleep(2)
        print("task %s done" %(self.n))

def do_main():
    for i in range(4):
        t = MyThread(i)
        t.start()
        # t.join()

if __name__ == '__main__':
    do_main()