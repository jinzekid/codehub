# Author: Jason Lu
# 支持大并发主要情况：遇到os操作就切换
import time

def func1():
    print("in func 1")
    time.sleep(5) # 做某些耗时的操作
    print("func1 exec done")

def func2():
    print("in func 2")
    time.sleep(3)  # 做某些耗时的操作
    print("func2 exec done")

def func3():
    print("in func 3")
    time.sleep(2)  # 做某些耗时的操作
    print("func3 exec done")


