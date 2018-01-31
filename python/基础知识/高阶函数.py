# Author: Jason Lu

def add(x, y, f):
    return f(x) + f(y)

def f(x):
    return abs(x)

ret = add(-10, 20, f)
print(ret) # output: 30