# Author: Jason Lu

a = (1, 2, 3, 4)
print(a.index(1)) # 返回参数在元组中的位置，如果没有的话会报异常

try:
    idx = a.index(0)
except ValueError as ve:
    print('Exception:', ve)

# 只读列表
tuple_names = ('alex', 'jack')
print(tuple_names.count('alex'))
print(tuple_names.index('alex'))
























