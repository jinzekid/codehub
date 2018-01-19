# Author: Jason Lu
import threading, time
def run(n):
    print("task:", n)
    time.sleep(2)
    print("task %s done", n)
    pass

# start_time = time.time()
# list_threads = []
# for i in range(5):
#     t = threading.Thread(target=run, args=(i,))
#     # 在当前主线程下生成5个线程
#     # 如果设置成为守护线程
#     # 当主线程结束的时候守护线程也会停止
#     t.setDaemon(True) # 开始守护线程
#     t.start()
#     list_threads.append(t)
#
# print("current active threads-----", threading.active_count())
# print("all threads finished-----", threading.current_thread())
# print("cost: %s" %(time.time()-start_time))

# 子线程中声明子线程
def son_run(n):
    print("son task:", n)
    time.sleep(2)
    print("son task %s done" % (n))

def parent_run(n):
    print("parent task:", n)

    # 创建5个守护子线程
    for i in range(5):
        t = threading.Thread(target=son_run, args=(i+1,))
        # t.setDaemon(True)
        t.start()

    time.sleep(1)
    print("parent task %s done" %(n))

def do_main():
    t_parent = threading.Thread(target=parent_run, args=(0,))
    t_parent.start()


if __name__ == '__main__':
    do_main()