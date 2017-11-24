# Author: Jason Lu
import sys
print(sys.getdefaultencoding())

s = "你好"
print(s)

s_gbk = s.encode("gbk")
print(s_gbk)
print(s.encode())

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print(gbk_to_utf8)

s_gb2312 = s.encode("gb2312")
print(s_gb2312)

gb2312_to_utf8 = s_gb2312.decode("gb2312").encode("utf-8")
print(gb2312_to_utf8)

print(gb2312_to_utf8.decode("utf-8"))