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

# r只读，w可写，a追加
print("\n============判断文件是否存在============\n")
# 读取文件，首先判断文件是否存在
try:
    fsock = open(str_filename, "r")
except IOError:
    print("The file don't exist, Please double check!")
    # exit()
print("\n============判断文件是否存在============\n")

print("\n============读取文件的内容============\n")
fsock = open(str_filename, "r")
AllLines = fsock.readlines()
for EachLine in AllLines:
    print(EachLine)
fsock.close()
print("\n============end 读取文件的内容============\n")

print("\n============覆盖文件内容============\n")
# 直接打开一个文件，如果文件不存在则创建文件
file_object = open(str_filename, 'w')
file_object.write("test")
file_object.close()
print("\n============end 覆盖文件内容============\n")

print("\n============追加文件内容============\n")
fsock = open(str_filename, "a")
fsock.write("""
#Line 1 Just for test purpose
#Line 2 Just for test purpose
#Line 3 Just for test purpose""")
fsock.close()
print("\n============end 追加文件内容============\n")

print("\n============判断文件是否关闭============\n")
# 判断文件是否关闭
S1 = fsock.closed
if S1:
    print('the file is closed')
else:
    print('The file donot close')
print("\n============end 判断文件是否关闭============\n")

fsock = open(str_filename, "w")
fsock.write(str(list_products))
fsock.close()
print("\n============读取文件的内容============\n")
fsock = open(str_filename, "r")
str_list = fsock.read()
fsock.close()

print(type(eval(str_list)))
print(eval(str_list)["Iphone"])

print("\n============end 读取文件的内容============\n")

