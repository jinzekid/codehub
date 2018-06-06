# Author: Jason Lu
import random

print(random.random())
print(random.randint(1, 3)) # 包含1和3
print(random.randrange(1, 3)) # 不包含3
print(random.choice("hello"))
print(random.choice([1,4,6]))
print(random.sample("abcdefghij", 3))
print(random.uniform(1, 3)) # 浮点数
# 洗牌功能
l = [1,2,3,4,5]
random.shuffle(l)
print(l)