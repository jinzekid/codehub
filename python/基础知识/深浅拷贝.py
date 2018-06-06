# Author: Jason Lu

import copy

name1 = ['name', ['a4', 100]]
print("====浅拷贝操作====")
# 方式一
p1 = copy.copy(name1) #浅拷贝
print(p1)
# 方式二
p2 = name1[:]
print(p2)
# 方式三
p3 = list(name1)
print(p3)

# 浅拷贝示例
# 创建联合账号
person = ['name', ['saving', 100]]
p1 = person[:]
p2 = person[:]

p1[0] = 'alex'
p2[0] = 'fengjie'
print(p1)
print(p2)

p1[1][1] = 50
print(p1)
print(p2)
'''
有个共同账号
['alex', ['saving', 100]]
['fengjie', ['saving', 100]]
'''
print("====end 浅拷贝操作====")
