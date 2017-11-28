# Author: Jason Lu

import time

# 本质就是一个函数，不修改原函数和调用方式
def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s", (stop_time - start_time))
    return warpper

@timmer
def test1():
    time.sleep(1)
    print("in the test1")

test1()

print("\n===============================\n")

def bar():
    time.sleep(1)
    print("in the bar")

def foo():
    print("in the foo")
    bar()
foo()

'''
实现装饰器知识储备：
1.函数即“变量”
2.高阶函数
    a：把一个函数名当做实参传给另外一个函数（不修改被装饰函数源代码的情况下，为其添加功能）
    b：返回值中包含函数名
3.嵌套函数
'''
print("\n===============以下情况只是满足了a条件================\n")

# 以下情况只是满足了a条件
# 高阶函数
# 利用高阶函数+嵌套函数=实现装饰器
def test1(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("the %s run time is %s", func, (end_time - start_time))

# 满足了条件a，但是没有满足条件b 改变了被调用函数的调用方式
test1(bar)

print("\n===============以下情况只是满足了b条件================\n")

def test2(func):
    print(func)
    return func

bar = test2(bar)
bar()

print("\n=============装饰器最终版本================\n")

# 先定义个高阶函数, 然后利用函数嵌套，最后实现装饰器功能
def f_gaojie_test(func):
    def f_deco():
        start_time = time.time()
        func()
        end_time = time.time()
        print("the %s run time is %s", func, (end_time - start_time))

    return f_deco

# 利用python的语法特性来实现直接运行方法，即可实现装饰器功能
@f_gaojie_test # 这句话相当于：f_test1 = f_gaojie_test(f_test1)
def f_test1():
    time.sleep(3)
    print("in the f_test1")

@f_gaojie_test # 这句话相当于：f_test2 = f_gaojie_test(f_test2)
def f_test2():
    time.sleep(3)
    print("in the f_test2")

f_test1()
f_test2()
