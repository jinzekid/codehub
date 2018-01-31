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

print()

# 获取列表长度
int_listlen = len(a)
print(int_listlen)

print()

list = ['apple', 'jack', 798, 2.22, 36]
otherlist = [123, 'xiaohong']

print(list)
print(list[0])
print(list[1: 3])
print(list[2: ])
print(otherlist * 2)
print(list + otherlist)

print()

names = ["111", "bbb", "ccc", ["111", "222"], "ddd"]
names2 = ["aaa", "bbb", "ccc"]
names.append("eee") #尾部添加
names.insert(1, "fff") #插入某个位置

print(names)
print(names[0], names[2]) #取第一个，第三个元素
print(names[0:3]) #顾头不顾尾 叫切片
print(names[-1]) #最后一个值
print(names[-2]) #最后第二个值
print(names[-3:-1]) #不包括最后一个值
print(names[-2:]) #取最后2个元素， 默认是[-2:-1]
print(names.count("111")) #打印有多少个eee元素
names.reverse() #翻转元素
print(names)

names.extend(names2) #拼接元素
print(names)
del names2 #删除变量

print("====for循环====")
for i in names:
    print(i)

print("====步长切片====")
print(names[::2]) #从0到-1，跳步长

# 浅拷贝
import copy
names22 = [["111", "222"], "ddd"]
names4 = names22.copy()
print(names4) #[['111', '222'], 'ddd']
names4[0][1] = 'why'
print(names4) #[['111', 'why'], 'ddd']
print(names22) #[['111', 'why'], 'ddd']

# 深拷贝
names5 = copy.deepcopy(names22)
print(names5) #[['111', 'why'], 'ddd']
names5[0][1] = 'time'
print(names5) #[['111', 'time'], 'ddd']
print(names22) #[['111', 'why'], 'ddd']

li = ['alex', 'eric', 'rain']
print("_".join(li))


# list基本操作
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


