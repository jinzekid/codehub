# Author: Jason Lu

# 方法一
'''
info = {
    "name": "alex",
    "age": 22
}

f = open("debug.txt", "w", encoding="utf-8")
f.write(str(info))

f.close()
'''

# 方法二 使用json进行序列化
'''
import json

def sayhi(n):
    print(n)

# 方法二 标准方法
info = {
    "name": "alex",
    "age": 22,
}
f = open("debug.txt", "w")
print(json.dumps(info))
f.write(json.dumps(info))

f.close()
'''

# 方法三
'''
# 相对于json，连函数都可以序列化，但是只能在python中使用
import pickle

def sayhi(n):
    print(n)

# 方法二 标准方法
info = {
    "name": "alex",
    "age": 22,
    "func": sayhi
}
f = open("debug.txt", "wb")
f.write(pickle.dumps(info))

f.close()
'''

# 方法四
'''
import pickle

def sayhi(n):
    print(n)

info = {
    "name": "alex",
    "age": 22,
    "func": sayhi
}
f = open("debug.txt", "wb")
pickle.dump(info, f)

f.close()
'''

# 方法五
'''
import json

# 方法二 标准方法
info = {
    "name": "alex",
    "age": 22,
}
f = open("debug.txt", "w")
f.write(json.dumps(info))

info["age"] = 21
f.write(json.dumps(info))

f.close()
'''