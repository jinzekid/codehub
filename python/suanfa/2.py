def deco_calu_func_time(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime as dt
        start = dt.now()
        ret = func(*args, **kwargs)
        delta = dt.now() - start
        print('func:' + func.__name__ + '------elapsed time:%.2f' %(delta.microseconds))
        return ret
    return wrapper

import random
list = [random.random() for i in range(100)]

#print(list)

#@deco_calu_func_time
def sort_mp(SList):
    #print("排序前:")
    #print(SList)

    for i in range(len(list)):
        for j in range(i):
            if SList[i] < SList[j]:
                tmp = SList[j]
                SList[j] = SList[i]
                SList[i] = tmp

    #print("排序后:")
    #print(SList)
    return SList

#@deco_calu_func_time
def sort_quick(array):
    if array is None:
        print("sort array can't be None!!")
        return None

    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        # 所有小于基准值
        less = [i for i in array[1:] if i <= pivot]

        # 所有大于基准值
        greater = [i for i in array[1:] if i > pivot]

        return sort_quick(less) + [pivot] + sort_quick(greater)

from datetime import datetime as dt
start = dt.now()
arr = sort_quick(list)
print(arr)
delta = dt.now() - start
print("elapsed time:", delta.microseconds)

start = dt.now()
arr = sort_mp(list)
print(arr)
delta = dt.now() - start
print("elapsed time:", delta.microseconds)






