# Author: Jason Lu

'''
f = open("yesterday2", "r", encoding="utf-8")
f_new = open("yesterday2.bak", "w", encoding="utf-8")

# 打开文件，修改完了，写到新文件中（效率高）
for line in f:
    # 循环查找字符串
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受", "肆意的快乐等Alex享受")

    # 每一行都要写入新文件
    f_new.write(line)


f.close()
f_new.close()
'''

# 改进版本
# 可以使用参数来进行替换
import sys

str_find = sys.argv[1]
str_replace = sys.argv[2]

print(str_find, str_replace)

f = open("yesterday2", "r", encoding="utf-8")
f_new = open("yesterday2.bak", "w", encoding="utf-8")

# 打开文件，修改完了，写到新文件中（效率高）
for line in f:
    # 循环查找字符串
    if str_find in line:
        line = line.replace(str_find, str_replace)

    # 每一行都要写入新文件
    f_new.write(line)


f.close()
f_new.close()