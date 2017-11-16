# Author: Jason Lu

import copy

name1 = ['name', ['a', 100]]

print("====浅拷贝操作====")
p1 = copy.copy(name1) #浅拷贝
print(p1)

p2 = name1[:]
print(p2)
print("====end 浅拷贝操作====")
