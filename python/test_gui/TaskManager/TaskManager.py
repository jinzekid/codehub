# Author: Jason Lu
import _thread as thread, time
import threading
from MyWindow import Ui_MainWindow as MainWindow
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
    mainWindow  = None

    def init_taskManager(self, func_refresh_del_task):
        self.timer = None
        self.listOfTasks = []
        self.removeTasks= []
        self.refresh_del_task  = func_refresh_del_task

        # 开启新线程
        thread.start_new_thread(self.do_task, ())
        pass

    def enqueue(self, task):
        if not task:return
        self.listOfTasks.append(task)
        print(">>新任务入队列 ")

    def dequeue(self, task):
        pass

    def get_list_of_tasks(self):
        return self.listOfTasks

    def do_task(self):
        while True:
            curTime = int(time.time())  # 获取时间戳
            print("cur time:" + str(curTime) + ", 任务数量: " + str(len(
                self.listOfTasks)))
            time.sleep(1)

            # 倒序循环删除
            for i in range(len(self.listOfTasks)-1, -1, -1):
                task = self.listOfTasks[i]
                if task.is_ready():
                    if task.is_start(curTime):
                        task.do_task()
                elif task.is_done():
                    self.refresh_del_task(task)
                    self.listOfTasks.pop(i)





