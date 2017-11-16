# Author: Jason Lu

print("====元组操作====")
import sys
import copy
index = int(input("input index:"))
names = ["111", "bbb", "ccc", ["111", "222"], "ddd"]
names2 = ["aaa", "bbb", "ccc"]
names.append("eee") #尾部添加
names.insert(1, "fff") #插入某个位置

print(names)
print(names[0], names[2]) #取第一个，第三个元素
print(names[index])
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
print("====end 元组操作====")

'''
print("====一般数据的拷贝====")
a = 1
b = a
b = 2
'''
#info = '''a={_a},b={_b}'''.format(_a=a,_b=b)
'''
print(info)
print("====end 一般数据的拷贝====")

print("====浅拷贝====")
names3 = names.copy() #拷贝一份
names3[3][0] = "jasonlu"
names3[3][1] = "jasonlu2"

print(names3)
print(names)
print("====end 浅拷贝====")

print("====深拷贝====")
names4 = copy.deepcopy(names) #拷贝一份
names4[3][0] = "jasonlu 333"
names4[3][1] = "jasonlu 444"
print(names4)
print(names)
print("====end 深拷贝====")

print("====for循环====")
for i in names:
    print(i)

print("====步长切片====")
print(names[::2]) #从0到-1，跳步长
'''


