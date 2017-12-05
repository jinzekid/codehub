# Author: Jason Lu

from collections import Iterable
from collections import Iterator
print(isinstance([], Iterable))

a = [1,2,3]
# 查看a中的方法
print(dir(a))

# 生成器一定是迭代器，因为有next方法
v = isinstance((x for x in range(5)), Iterator)
print(v)

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
b = iter(a)
print(isinstance(b, Iterator))

c = ()
# c = iter(c) # 转换成迭代器
print(isinstance(c, Iterator))