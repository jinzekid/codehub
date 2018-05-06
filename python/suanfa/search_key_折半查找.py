def binary_search(list, low, high, key):
    if low > high:
        print("Not Found!")
        return -1

    mid = int((low + high) / 2)
    print('mid:%s, low:%s, high:%s' %(mid, low, high))
    if list[mid] == key:
        print("Find key at index: %s" %mid)
        return mid

    if key > list[mid]:
        low = mid + 1
        binary_search(list, low, high, key)
    elif key < list[mid]:
        high = mid -1
        binary_search(list, low, high, key)


list = [1,2,5,6,8,9]

#binary_search(list, 0, len(list), 5)

str_input_key = ''
from datetime import datetime as dt
while True:
    str_input_key = input('请输入要查找的数值(q或Q退出):')

    if str_input_key in ['q', 'Q']:
        break

    start = dt.now()
    int_ret = binary_search(list, 0, len(list)-1, int(str_input_key))
    delta = dt.now() - start
    print("elapsed time:", delta.microseconds)

    #print(int_ret)

    '''
    #if int_ret is not None:
    #    print("恭喜你!!!")
    #else:
    #    print("很抱歉，没有找到!!!")
    '''

