# Author: Jason Lu

# 非0 就是真
print(all([0, -1]))
print(any([1]))
print(ascii([1, 2, "这个测试"]))
# 十进制转二进制
print(bin(1))
print(bin(255))
a = bytes("abcde", encoding="utf-8")
print(a.capitalize(), a)
b = bytearray("abcd", encoding="utf-8")
print(b[1])
b[1] = 100
print(b)
# 判断是否是方法
print(callable(a))
# 字符串可以转成可执行代码
# compile()
# dir 显示对象中可以执行的方法
print(dir(a))
print(divmod(5, 3))
def sayhi(n):
    print("hi:", n)
sayhi(3)
# 匿名函数
# (lambda n:print(n))(5)
calc = lambda n: print(n)
calc(5)

# lambda 需要结合使用
ret = filter(lambda n: n > 5, range(10))
print(type(ret))
for i in ret:
    print(i)

ret = map(lambda n: n**n, range(10))
print(type(ret))
for i in ret:
    print(i)

import functools
ret = functools.reduce(lambda x, y: x+y, range(10))
print(ret)

a = frozenset(set([1, 4, 333, 212, 33, 33, 12, 4]))

def test():
    local_var = 333
    print(locals())
    print(globals()) # 没有局部变量local_var

# 整个程序的所有的key value
print(globals())
test()
print(hash("jason"))
print(hex(255)) #16进制
print(oct(8)) #8进制

a = {6:2, 8:0, 1:4, -5:6, 99:11, 4:22}
# sorted(a4)
# 默认按照key排序
print(sorted(a.items()))
# 默认按照value排序
print(sorted(a.items(), key=lambda x: x[1], reverse=True))

# zip按照最小的进行key value组合
a = [1, 2, 3, 4, 5, 6]
b = ["a4", "b", "c", "d"]
ret = zip(a, b)
print(type(ret))
for i in ret:
    print(i)

# 引入代码， 并且执行，感觉类似模块功能
__import__("生成器")

























