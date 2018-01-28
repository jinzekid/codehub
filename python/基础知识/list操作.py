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


