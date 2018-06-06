# Author: Jason Lu
import time

# 函数定义
def func1():
    print('I\'m a4 function')
    return 0

x = func1()

# 定义过程，没有返回值
def func2():
    print('I\'m a4 process')

y = func2()

print(type(x), type(y)) #<class 'int'> <class 'NoneType'>

print()


# 使用函数的好处
# 可扩展
# 一致性
# 便易维护
def logger():
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    with open("a4.txt", "a4+") as f:
        time.sleep(1)
        f.write("%s end action\n" %time_current)


def func_test1():
    print("func_test1 starting action....")
    logger()

def func_test2():
    print("func_test2 starting action....")
    logger()

def func_test3():
    print("func_test3 starting action....")
    logger()

# func_test1()
# func_test2()
# func_test3()


print("\n------------------我是分割符------------------\n")
# 返回值
def func_test4():
    print("func_test4 in action...")
    return 1, "hello", ["alex","wepeiqi"], {"name":"alex"}

ret = func_test4()
print(ret, type(ret)) # 返回元组


# 固定位置参数
def func_test5(x, y):
    print(x)
    print(y)

func_test5(19, 20)

def func_test6(x, y):
    print(x)
    print(y)

func_test6(10, y=20)


# 默认参数
def func_test7(x=1, y=2):
    print(x)
    print(y)

func_test7()
func_test7(10)

print("\n------------------我是分割符------------------\n")
# 不确定参数个数
# args接受n个位置参数，转换成元组的形式
def func_test8(*args):
    for v in args:
        print(v)

func_test8(1, 2, [2, 3, 4, 4])


# kwargs把n个关键字参数，转换成字典的方式
def func_test9(**kwargs):
    print(kwargs)

    for k in kwargs.keys():
        if k == "name":
            print(kwargs[k])

func_test9(name="alex", age=8, sex="F", list=[1,3,4])
func_test9(**{"name": "alex", "age": 8})


def func_test10(name, **kwargs):
    print(name)
    print(kwargs)

def func_test11(name, age = 18, **kwargs):
    print(name)
    print(age)
    print(kwargs)

func_test11("alex", sex="m", hobby="tesla", age=3)
func_test11("alex", 20, sex="m", hobby="tesla")


def func_test12(name, age=18, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

func_test12("alex12", 100, 1, 2, 3, sex="m", hobby="tesla")


# 匿名函数
calc = lambda x: x*3
print(calc(3))







