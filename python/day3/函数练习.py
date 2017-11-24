# Author: Jason Lu

import time

# 定一个函数
def func1():
    print("I'm a function!")
    return 0

x = func1()


# 定一个过程
def func2():
    print("I'm process!")

y = func2()

print(type(x), type(y))

# with open("a.txt", "ab") as f:
#     f.write("end action")

# 使用函数的好处
def logger():
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    with open("a.txt", "a+") as f:
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

def func_test4():
    print("func_test4 in action...")
    return 1, "hello", ["alex","wepeiqi"], {"name":"alex"}

ret = func_test4()
print(ret, type(ret))

def func_test5(x, y):
    print(x)
    print(y)

func_test5(19, 20)


def func_test6(*args):
    for v in args:
        print(v)

func_test6()

def func_test7(x=1, y=2):
    print(x)
    print(y)

func_test7()
func_test7(10)

def func_test8(x, y):
    print(x)
    print(y)

func_test8(10)


