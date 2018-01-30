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

