# Author: Jason Lu
def format_time(ttime):
    '''
    进行时间格式化输出
    :param ttime: 时间（单位秒）
    :return: 时间格式输出：00:00:00
    '''
    hours = int(ttime / (60*60))
    left_m = ttime-hours*3600
    minutes = int(left_m / 60)
    left_s = left_m - minutes*60
    seconds = int(left_s % 60)

    str_time = ''

    if hours >= 10:
        str_time += str(hours)
    else:
        str_time += '0' + str(hours)
    str_time += ':'

    if minutes >= 10:
        str_time += str(minutes)
    else:
        str_time += '0' + str(minutes)
    str_time += ':'

    if seconds >= 10:
        str_time += str(seconds)
    else:
        str_time += '0' + str(seconds)

    return str_time

# 文件或文件夹复制
def cpy_file(fromDir, toDir, fileName):
    '''
    复制文件
    :param fromDir: 源目录
    :param toDir: 目标目录
    :param fileName: 文件名
    :return: 是否复制成功
    '''
    import shutil
    import os
    if not fileName or not fromDir or not toDir:
        return

    print(fromDir +" -- " + toDir + " -- " + fileName)
    src_file_name = fromDir + '/' + fileName
    if os.path.isdir(src_file_name): # 文件夹类型
        print(src_file_name +" to " + toDir)
        # 判断文件是否存在
        # 如果存在先删除
        destDir = toDir + '/' + fileName + '/'
        if os.path.exists(destDir):
            shutil.rmtree(destDir)
        # 复制文件夹内容
        srcDir = src_file_name + '/'
        shutil.copytree(srcDir, destDir)
    else:
        shutil.copy(src_file_name, toDir)

# 队列类
class PQueue(object):
    def __init__(self):
        self.list = []
        self.front = 0
        self.rear = 0

        self.lengthSize = 0
        self.MAX_TASK_SIZE = 3;
        self.MAX_SIZE = (self.MAX_TASK_SIZE+1)
        pass

    def clear(self):
        for item in self.list:
            item = None
        self.front = 0
        self.rear  = 0
        self.lengthSize = 0
        pass

    def destory(self):
        self.clear()
        self.list  = None
        pass

    def dequeue(self):
        if self.is_empty():
            return False
        task = self.list[self.front]
        self.front += 1
        self.lengthSize -= 1
        return task

    def enqueue(self, task):
        if self.is_full():
            return False

        self.list.append(task)
        self.rear = (self.rear + 1) % self.MAX_SIZE
        self.lengthSize += 1
        return True

    def is_empty(self):
        if self.rear == self.front:
            return True
        return False

    def is_full(self):
        if (self.rear+1) % self.MAX_SIZE == self.front:
            return True
        return False

    def get_length(self):
        return self.lengthSize

    def traverse_tasks(self):
        print("-------------------")
        print("task size:" , self.lengthSize)
        tmp_front = self.front
        tmp_rear = self.rear
        while tmp_front != tmp_rear:
            print(self.list[tmp_front])
            tmp_front += 1

        print("-------------------")



