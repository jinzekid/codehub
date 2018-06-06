# Author: Jason Lu
msg = "我爱北京天安门"
print(msg)
print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))


# b只能用于ascii码
msg2 = 'this is test'
print(msg2)

print(msg.encode(encoding="gb2312"))
print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-16"))
print(msg.encode(encoding="utf-32"))

# 转码规则：
print(msg2.encode(encoding="utf-32"))
print(msg2.encode(encoding="utf-16").decode(encoding="utf-16"))

print()
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