# Author: Jason Lu
import _thread as thread, time
import threading

class TaskManager(object):
    def __init__(self):
        self.timer = None
        self.listOfTasks = []

        # 开启新线程
        thread.start_new_thread(self.do_task, ())
        pass

    def enqueue(self, task):
        if not task:return
        self.listOfTasks.append(task)
        print(">>新任务入队列 ")

    def dequeue(self, task):
        pass

    def do_task(self):
        return
        while True:
            curTime = int(time.time())  # 获取时间戳
            print("cur time:" + str(curTime))
            time.sleep(1)

            for task in self.listOfTasks:
                print("tasks:" + task.nameOfTask)







