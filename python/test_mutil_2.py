# Author: Jason Lu
import threading
import time
import random
from random import Random
from threading import Thread, Lock
from multiprocessing import Process


class TaskManager(object):
    _tasks = []

    def add_task(self, task):
       if not task in self._tasks:
           self._tasks.append(task)

    def start_all_tasks(self):
        for task in self._tasks:
            task.start()

    def notify(self, complete_task):
        print(">>:已经完成的任务:%s" % complete_task)
        # 移除任务
        if complete_task in self._tasks:
            self._tasks.remove(complete_task)

        print(">>:剩余任务数量:%d" % (len(self._tasks)))

    @property
    def tasks(self):
        return self._tasks


class TaskThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self._observers = []

    def run(self):
        print(">>:%s thread is running" % self.name)
        wait_time = random.randint(1, 5)
        time.sleep(wait_time)
        self.notify()

    def register_ob(self, ob):
        self._observers.append(ob)
        print(">>:self.name=%s, length=%d" %\
              (self.name, len(self._observers)))
        pass

    def remove_ob(self, ob):
        self._observers.remove(ob)
        pass

    def notify(self):
        for ob in self._observers:
            ob.notify(self)


def wait_all_task_complete(tasks):
    while True:
        if len(tasks) <= 0:
            break
            #print(">>:管理器正在检查任务状态...")
        else:
            print(">>:所有任务完成...:)")

def start_thread(func_complete, task):
    t = threading.Thread(target=func_complete, args=(task,))
    t.start()

tm = TaskManager()
for i in range(5):
    task = TaskThread()
    tm.add_task(task)
    task.register_ob(tm)
    #task.start()

print(tm.tasks)
start_thread(wait_all_task_complete, tm.tasks)

tm.start_all_tasks()



