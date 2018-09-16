from datetime import datetime as dt 
# 装饰器-测试函数运行时间
def time_calcuate(func):
    def inner(*args, **kwargs):
        start = dt.now()
        ret = func(*args, **kwargs)
        delta = dt.now() - start 
        print('elapsed time:' , delta.microseconds)
        return ret   
    return inner 


"""
@time_calcuate
def func_test(p1, p2, p3):
    #... 
    return

ret = func_test(p1,p2,p3)
"""
