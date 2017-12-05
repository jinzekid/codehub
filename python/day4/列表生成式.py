# Author: Jason Lu

# 固定列表
a = [1, 2, 3]
print(a)

# 动态生成列表
ret = [ i*2 for i in range(10) ]
print(ret)

# 相当于以下代码
a = []
for i in range(10):
    a.append(i * 2)
print(a)

