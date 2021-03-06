# Author: Jason Lu
# enum.Enum 枚举类型
import os
from PyQt5.QtCore import QThread, pyqtSignal, QObject, QDateTime
from collections import namedtuple
from enum import Enum
import LYUtils as utils

# 枚举：任务状态
class TaskStatus(Enum):
    none  = 0
    ready = 1
    start = 2
    doing = 3
    done  = 4



import _thread as thread, time
import threading
import hashlib

class CpyTask(object):

    """
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)

    # 处理业务逻辑
    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currTime))
            time.sleep(1)
    """

    def init_task(self, name, src_path, dest_path, srcOfFiles, dt):
        self.status = TaskStatus.none
        self.desofFiles = []
        self.srcPath = src_path
        self.destPath = dest_path
        self.srcOfFiles = srcOfFiles
        self.dt = dt
        self.name = name
        m1 = hashlib.md5()
        info = self.srcPath + '-' + self.destPath + '-' + str(self.srcOfFiles) + '-' + self.name
        m1.update(info.encode('utf-8'))
        self.taskToken = m1.hexdigest()
        
        curTime = int(time.time())  # 获取时间戳
        self.leftTime = self.dt - curTime

        self.status = TaskStatus.ready

        """
        tmp = ''
        for name in self.srcOfFiles:
            tmp += ' ' + name
        tmp += self.srcPath
        tmp += self.destPath

        if name == '' or name == None:
            self.name = hashlib.md5(tmp)
        else:
            self.name = name
        """

        print('>>:task info:',
              self.name,
              self.srcPath,
              self.destPath,
              self.srcOfFiles,
              self.dt,
              self.taskToken)
        return self


    def update_task_info(self, curTime):
        self.leftTime = self.dt - curTime

    def is_start(self, curTime):
        if curTime == self.dt:
            return True
        return False

    def do_task(self):
        print("task " + self.name + ", doing...")
        print("source path:" + self.srcPath)
        print("dest path:" + self.destPath)

        if self.destPath == '':
            print(">>:destination path is empty")
            return

        if self.srcPath == '':
            print(">>:source path is empty")
            return

        for file in self.srcOfFiles:
            utils.cpy_file(self.srcPath, self.destPath, file)

        #self.update_dir_files(self.listWidgetOfDest, self.destPath)
        print(">>:task finish...")

        self.status = TaskStatus.done

    def is_ready(self):
        return self.status == TaskStatus.ready

    def is_done(self):
        return self.status == TaskStatus.done

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
