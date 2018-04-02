# Author: Jason Lu
import sys
from datetime import datetime
import numpy as np

"""
python中的向量加法
n为指定向量大小的整数
对比纯python代码和NumPy代码
两个返回的对象类型不一样
"""
def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in list(range(len(a))):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])

    return c

size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
print(type(c)) # <class 'list'>
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("PythonSum elapsed time in microseconds", delta.microseconds)
start = datetime.now()
c = numpysum(size)
print(type(c)) # <class 'numpy.ndarray'>
delta = datetime.now() - start
print("The last 2 elements of the sum", c[-2:])
print("NumPySum elapsed time in microseconds", delta.microseconds)


