# Author: Jason Lu

list_1 = [1, 4, 5, 7, 3, 6, 7, 9]
#集合转换
list_1 = set(list_1)
print(list_1, type(list_1))
list_2 = set([2, 6, 0, 66, 22, 8, 4])
print(list_1, list_2)
# 求交集
list_jj = list_1.intersection(list_2)
print(list_jj)
# 求并集
print(list_1.union(list_2))
# 求差集
print(list_1.difference(list_2))
# 判断子集
list_3 = set([1, 4])
print(list_3.issubset(list_1))
print(list_1.issuperset(list_2))
# 对称差集（互相没有取出来，把相同的剔除掉）
print(list_1.symmetric_difference(list_2))
# 如果没有交集返回true，有交集返回false
list_4 = set([1, 3, 7])
list_5 = set([5, 6, 8])
print(list_4.isdisjoint(list_5))

print("\n----------------运算符----------------\n")
# 交集
print(list_1 & list_2)
# 并集
print(list_2 | list_1)
# 差集 in list_1 but not in list_2
print(list_1 - list_2)
# 对称差集
print(list_1 ^ list_2)

print("\n----------------基本操作----------------\n")
list_1.add(99)
print(list_1)
list_1.update([10, 20, 3])
print(list_1)
len(list_1)
# 列表，字典，集合，字符串都是这么写
# 判断是否在里面都是x in xxx
isIn = 1 in list_1
print(isIn)
list_1.pop()
print(list_1)
list_1.discard(99)
print(list_1)









