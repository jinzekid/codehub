# Author: Jason Lu

import sys

# with的作用自动关闭文件
with open("yesterday2", "r", encoding="utf-8") as f:
    print(f.readlines())

with open("yesterday2", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
# py2.7以后可以打开多个文件
with open("yesterday2", "r", encoding="utf-8") as f, \
     open("yesterday2", "r", encoding="utf-8") as f2:
    for line in f:
        print(line)