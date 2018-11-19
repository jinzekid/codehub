# Author: Jason Lu
# enum.Enum 枚举类型
from collections import namedtuple
from enum import Enum

class TaskStatus(Enum):
    none  = 0
    ready = 1
    start = 2
    doing = 3


import _thread as thread, time
import threading
import hashlib

class MyCpyTask(object):
    def __init__(self):
        self.srcOfFiles = [] # 需要上传的文件列表
        self.desofFiles = []
        self.dt = 0
        self.src_path = ''   # 源路径
        self.dest_path = ''   # 目标路径
        self.t = None
        self.nameOfTask = '' #self.src_path + '->' + self.dest_path
        self.status = TaskStatus.none

    def init_task(self, name, src_path, dest_path, srcOfFiles, dt):
        """
        初始化任务
        :param src_path:
        :param dest_path:
        :param srcOfFiles:
        :param dt:
        :return:
        """
        self.src_path = src_path
        self.dest_path = dest_path
        self.srcOfFiles = srcOfFiles
        self.dt = dt

        self.status = TaskStatus.ready


        tmp = ''
        for name in self.srcOfFiles:
            tmp += ' ' + name
        tmp += self.src_path
        tmp += self.dest_path

        if name == '' or name == None:
            self.nameOfTask = hashlib.md5(tmp)
        else:
            self.nameOfTask = name

        print('>>:task info:',
              self.nameOfTask,
              self.src_path,
              self.dest_path,
              self.srcOfFiles,
              self.dt)
        return self

    def start_task(self):
        if self.status == TaskStatus.ready:
            self.status = TaskStatus.doing
        """
        print(self.dateObj.text())
        print(self.dateObj.dateTime())
        taskQDateTime = int(self.dateObj.dateTime().toTime_t())
        print("task time:" + str(taskQDateTime))
        curTime = int(time.time()) #获取时间戳
        print("cur time:" + str(curTime))

        self.dt = taskQDateTime - curTime - 1 # -1是为了有大概秒的误差
        print("dt:" + (utils.format_time(self.dt)))
        # 开始倒计时
        self.init_count_down_timer(self.timer)
        """
        #thread.start_new_thread(self.do_task, ())
        pass

    def do_task(self):

        while self.dt > 0:
            time.sleep(1)
            print(self.nameOfTask , " >>left time:" , str(self.dt))
            self.dt -= 1

        print(">>:task finish...")

"""
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
"""