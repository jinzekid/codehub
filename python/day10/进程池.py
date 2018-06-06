# Author: Jason Lu
# 比如数据库的连接，只需要在父进程中连接一个连接，提高了效率

from  multiprocessing import Process, Pool
import time


def Foo(i):
    time.sleep(2)
    return i + 100


def Bar(arg):
    print('-->exec done:', arg)


pool = Pool(processes=5) # 允许同时放入5个进程

for i in range(10):
    pool.apply_async(func=Foo, args=(i,), callback=Bar) # 并行，callback=回调
    # pool.apply(func=Foo, args=(i,)) # 实际上变成了串行
    # pool.apply_async(func=Foo, args=(i,)) # 串行


print('end')
pool.close()
pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。