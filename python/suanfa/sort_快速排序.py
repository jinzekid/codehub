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
arr = sort_quick([3,42,10,2,130,20])
print(arr)
delta = dt.now() - start
print("elapsed time:", delta.microseconds)






