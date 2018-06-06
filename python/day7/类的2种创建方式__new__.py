# Author: Jason Lu

class Foo(object):

    def __init__(self, name):
        self.name = name

# 普通方式
f = Foo("alex")
print(f.name)
print(type(f))
print(type(type(f)))


# 特殊方式
def func(self):
    print('hello wupeiqi')


Foo2 = type('Foo', (object,), {'func': func})
f2 = Foo2()
f2.func()
# type第一个参数：类名
# type第二个参数：当前类的基类
# type第三个参数：类的成员




