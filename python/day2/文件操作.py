# Author: Jason Lu
# 购物车：
#     用户入口：
#         1。商品信息存在文件里
#         2。已购商品，余额记录。（下一次不需要输入工资）
#
#     商家入口：
#         1。可以天际商品，修改商品价格


import os, sys

str_filename = '/Users/jasonlu/Desktop/thefile.txt'

# 商品列表
list_products = {
                    'Iphone': 5800,
                    'Mac Pro': 12000,
                    'Starback Latte': 31,
                    'Alex Python': 81,
                    'Bike': 800
                 }

str_filename = "testFile"
# r只读，w可写，a追加
print("\n============判断文件是否存在============\n")
# 读取文件，首先判断文件是否存在
try:
    fsock = open(str_filename, "r")
except IOError:
    print("The file don't exist, Please double check!")
    # exit()

print("\n============读取文件的内容============\n")
fsock = open(str_filename, "r")
AllLines = fsock.readlines()
for EachLine in AllLines:
    print(EachLine)
fsock.close()

print("\n============覆盖文件内容============\n")
# 直接打开一个文件，如果文件不存在则创建文件
file_object = open(str_filename, 'w')
file_object.write("debug")
file_object.close()

print("\n============追加文件内容============\n")
fsock = open(str_filename, "a")
fsock.write("""
#Line 1 Just for debug purpose
#Line 2 Just for debug purpose
#Line 3 Just for debug purpose""")
fsock.close()

print("\n============判断文件是否关闭============\n")
# 判断文件是否关闭
S1 = fsock.closed
if S1:
    print('the file is closed')
else:
    print('The file donot close')

fsock = open(str_filename, "w")
fsock.write(str(list_products))
fsock.close()
print("\n============读取文件的内容============\n")
fsock = open(str_filename, "r")
str_list = fsock.read()
fsock.close()

print(type(eval(str_list)))
print(eval(str_list)["Iphone"])

print("\n============其他============\n")

str_filename2 = '/Users/jasonlu/Desktop/Dev/GitHub/codehub/python/day3/1.txt'
'''
# 直接读取文件内容
# data = open(str_filename2, encoding="utf-8").read()
# print(data)
'''
# f为文件句柄
'''
f = open(str_filename2, encoding="utf-8")
data = f.read()
data2 = f.read()
print(data)
print(data2)
f.close()
'''

# f = open("yesterday2", "a", encoding="utf-8")
# f.write("\n我爱北京天安门........\n")
# f.write("天安门上太阳升....")
# f.close()

f2 = open("yesterday2", "r", encoding="utf-8")
print(f2.tell()) #打印当前位置
print(f2.readline())
print(f2.readline())
print(f2.readline())
print(f2.tell())
f2.seek(0)
print(f2.readline())
print(f2.name)

# 文件缓存机制
# 达到一定大小，一次性写入
# 场景：要求实时的一致性强，强制刷新
f2.flush()
f2.close()

f2 = open("yesterday2", "a", encoding="utf-8")
f2.write("hello 1")

# 从文件开头截断
f2.truncate()
f2.close()


f2 = open("yesterday2", "w", encoding="utf-8")
# 从文件开头截断
f2.truncate()
f2.close()

print("\n============我是分隔符============\n")

'''
print("--------我是分割线--------")
# 一行一行读取，内存中只保存一行
# 效率高
count = 0
for line in f2:
    count += 1
    if count == 9:
        print("----------")
        continue

    print(line.strip())
'''

'''
# 全部读取，浪费内存，时间
for index, line in enumerate(f2.readlines()):
    if index == 9:
        print("----------")
        continue
    print(line.strip())
f2.close()
'''

'''
print("\n============修改文件的内容============\n")
# 读写 打开读写
f2 = open("yesterday2", "r+", encoding="utf-8")
print(f2.readline())
print(f2.readline())
print(f2.readline())
print(f2.tell()) # 打印光标
f2.write("----------kao-----------")
print(f2.readline())
f2.close()
'''

'''
# 写读
f2 = open("yesterday2", "w+", encoding="utf-8")
f2.write("----------kao-----------\n")
f2.write("----------kao-----------\n")
f2.write("----------kao-----------\n")
f2.write("----------kao-----------\n")

print(f2.tell()) # 打印光标
# f2.seek(10) # 没有办法定位修改 只能追加
print(f2.readline())
f2.write("should be at the begining of the second line.")
f2.close()
'''

'''
# 以二进制文件读 比如视频
# 使用场景:
#   网络传输（socket）
#   视频文件
f2 = open("yesterday2", "rb")
print(f2.readline())
print(f2.readline())
print(f2.readline())
f2.close()
'''

'''
# 以二进制文件写 比如视频
f2 = open("yesterday2", "ab")
f2.write(("hello binary\n").encode())
f2.close()
'''
