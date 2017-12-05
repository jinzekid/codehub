# Author: Jason Lu

# 方法一 不标准
'''
f = open("debug.txt", "r", encoding="utf-8")
data = f.read()
data = eval(data)
print(data["name"])
f.close()
'''

# 方法二 标准用法
'''
import json
f = open("debug.txt", "r", encoding="utf-8")

data = json.loads(f.read())
print(data["name"])

f.close()
'''

# 方法三
'''
import pickle

def sayhi(name):
    print("hello: ", name)

f = open("debug.txt", "rb")
data = pickle.loads(f.read())

# 只要方法名字一样一样可以执行
print(data["func"]("jason"))

f.close()
'''

# 方法四
'''
import pickle

def sayhi(name):
    print("hello: ", name)

f = open("debug.txt", "rb")
data = pickle.load(f)

# 只要方法名字一样一样可以执行
print(data["func"]("jason"))

f.close()
'''

# 方法五 会报错，一般dump一次，load一次
'''
import json
f = open("debug.txt", "r", encoding="utf-8")

# 报错
for line in f:
    print(json.loads(line))

# 报错
data = json.loads(f.read())
print(data)

f.close()
'''


































