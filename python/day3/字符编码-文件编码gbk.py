#-*-coding:gbk-*-
# ???????????
# Author: Jason Lu

s = "???"
print(s)

print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312"))