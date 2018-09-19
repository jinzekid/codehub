# Author: Jason Lu
# 进程管理器
# 用于创建管理进程
from threading import Thread, Lock
from multiprocessing import Process
import time


# 进程管理类，也是一个观察者，观察所有的进程状态
class ProcessManager(Process):
    #     _instance_lock = Lock() # 单利锁
    #     _list_process = []

    #     def __init__(cls, *args, **kwargs):
    #         if not hasattr(ProcessManager, '_instance'):
    #             with ProcessManager._instance_lock:
    #                 if not hasattr(ProcessManager, '_instance'):
    #                     ProcessManager._instance = object.__new__(cls)
    #         return ProcessManager._instance

    def __init__(self):
        Process.__init__(self)
        self._list_process = []
        print(">>:创建ProcessManager:%s" % self.name)

    def attch(self, process):
        if not process in self._list_process:
            print(">>:新进程加入...%s" % process)
            self._list_process.append(process)
            print(">>:length list_process:%d" % len(self._list_process))
            print(">>:_list_process:%s" % id(self._list_process))

    # 只要有任务加入就应该执行
    def run(self):
        #         print(">>:ProcessManager:%s" % self.name)
        #         print(self._list_process)
        while True:
            #             print(">>:ProcessManager:%s" % self.name)
            #             print(">>:length list_process:%d" % len(self._list_process))
            #             print(">>:_list_process:%s" % id(self._list_process))
            if len(self._list_process) > 0:  # 如果栈内有任务，就直接执行
                #                 for taskProcess in self._list_process:
                for i in range(len(self._list_process)):
                    taskProcess = self._list_process[i]
                    if taskProcess.active:
                        print('>>:process active: %s' % taskProcess.active)
                        taskProcess.start()
                        taskProcess.join()
                        self._list_process.pop() # 进程出栈并执行

                        print('>>:新进程%s开始启动...' % taskProcess)

    def update(self, process, func_complete):
        print('>>:ProcessManage 监测到进程 %s 结束了' % process)
        print('>>:该进程最后完成的执行任务=======')
        func_complete()
        print('==============================')


# 自定义基类进程，可以添加观察者
class TaskProcess(Process):
    def __init__(self, active=False, interval=0, task=None, complete=None):
        Process.__init__(self)
        self.task = task
        self.complete = complete
        self.active = active
        self.interval = interval
        self._obs = []  # 用于添加观察者

    # 添加观察者
    def register_ob(self, ob):
        print("------")
        print(ob)
        print("------")
        if not ob in self._obs:
            self._obs.append(ob)
            print('>>:添加新的观察者:%s' % ob)

    # 移除观察者
    def unregister_ob(self, ob):
        try:
            self._obs.remove(ob)
            print('>>:取消观察者:%s' % ob)
        except ValueError as ve:
            print("Exception %s:" % ve)

    # 通知所有观察者
    def notify(self):
        for ob in self.obs:
            ob.update(os.getpid(), self.complete)

    # 重写process类的run方法
    def run(self):
        t_start = time.time()
        time.sleep(self.interval)

        if self.task:
            self.task()

        t_stop = time.time()
        print("%s 执行结束，耗时%.2f" % (os.getpid(), t_stop - t_start))

        # 线程结束啦，通知所有观察者
        self.notify()


def task_download():
    print(">>:当前执行的任务: %s" % '开始下载')


def func_complete_download(name):
    print(">>:完成任务: %s" % 'ssss')


if __name__ == '__main__':
    pm = ProcessManager()
    p_download = TaskProcess(True, 5, task_download, func_complete_download)
    pm.attch(p_download)
    p_download.register_ob(pm)

    pm.start()
    # time.sleep(3)
    print('开启进程....')
    p_download.active = True