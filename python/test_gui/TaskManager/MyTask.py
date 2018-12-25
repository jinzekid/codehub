# Author: Jason Lu
# enum.Enum 枚举类型
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
    def __init__(self):
        self.srcOfFiles = [] # 需要上传的文件列表
        self.desofFiles = []
        self.dt = 0
        self.srcPath = ''   # 源路径
        self.destPath = ''   # 目标路径
        self.t = None
        self.name = '' #self.src_path + '->' + self.dest_path
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
        self.srcPath = src_path
        self.destPath = dest_path
        self.srcOfFiles = srcOfFiles
        self.dt = dt

        self.status = TaskStatus.ready

        tmp = ''
        for name in self.srcOfFiles:
            tmp += ' ' + name
        tmp += self.srcPath
        tmp += self.destPath

        if name == '' or name == None:
            self.name = hashlib.md5(tmp)
        else:
            self.name = name

        print('>>:task info:',
              self.name,
              self.srcPath,
              self.destPath,
              self.srcOfFiles,
              self.dt)
        return self

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