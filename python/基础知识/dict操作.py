# Author: Jason Lu

dict = {}

dict['one'] = 'This is one'
dict[2] = 'This is two'

tinydict = {'name': 'john', 'code': 5644, 'dept': 'sales'}

print(dict['one'])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

print(dict)
del dict[2]
print(dict)

print(dict.pop('one'))

c = dict.fromkeys([6, 7, 8], "debug") #初始化一个新的字典
print(c)

info = c
# 字典循环
print("\n============字典循环============\n")

# 更高效
for i in info:
    print("tt:", i, info[i])

print("\n========================\n")


# 有个字典把列表的过程，效率低下
for k, v in info.items():
    print(k, v)

print("\n============end of 字典操作============\n")


# 深浅copy
c = dict.fromkeys([6, 7, 8], [1, {"name": "alex"}, 444]) #初始化一个新的字典
print(c)
c[7][1]["name"] = 'jason'
print(c)






















