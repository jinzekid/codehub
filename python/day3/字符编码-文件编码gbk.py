#-*-coding:gbk-*-
# 这是文件编码
# Author: Jason Lu

s = "你好"
print(s)

print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312"))