# Author: Jason Lu
import _thread as thread, time
import threading
# 单例模式
# 使用__new__方法
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

# 装饰器版本
def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class TaskManager(object):

    listOfTasks = []
    timer       = None

    def init_taskManager(self):
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
        while True:
            curTime = int(time.time())  # 获取时间戳
            print("cur time:" + str(curTime) + ", 任务数量: " + str(len(
                self.listOfTasks)))
            time.sleep(1)

            for task in self.listOfTasks:
                if task.is_ready():
                    print("task id:" + str(id(task)))

                    if task.is_start(curTime):
                        task.do_task()


            # 更新任务列表数量
            for i in range(len(self.listOfTasks)):
                task = self.listOfTasks[i]
                if task.is_done():
                    # 销毁任务
                    print("del task: " + str(id(task)))
                    del self.listOfTasks[i]








