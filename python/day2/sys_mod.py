# Author: Jason Lu

'''
import sys

print(sys.path) #打印环境变量
print(sys.argv)  #打印脚本相对路径
# print(sys.argv[2]) #取输入参数第n个参数（从0开始）

import os
# cmd_res = os.system('ls')
# cmd_res = os.popen("ls") #打印内存对象地址
cmd_res = os.popen("ls").read() #通过read方法读取
print("--->", cmd_res)

# 当前目录下创建目录
os.mkdir("new_dir")
'''

from new_dir import login



