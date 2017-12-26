# Author: Jason Lu
# 1.先把方法变成一个属性
# 2.然后赋值
# 3.然后调用

class Dog(object):
    # 类变量
    # n = 333
    name = "ahaha"

    def __init__(self, name):
        self.name = name
        self.__food = None

    # 属性方法
    @property
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))

    # 如果想要赋值再写一个eat方法, 需要单独写且必须一样
    @eat.setter
    def eat(self, food):
        self.__food = food
        print("set to food:", food)

    # 删除属性方法
    @eat.deleter
    def eat(self):
        del self.__food
        print("删除完了...")

    def talk(self):
        print("%s is talking.." %self.name)

######################################################
d = Dog("dog")
print(d.__doc__)


d.eat
d.eat = "bbcc" # 首先赋值
d.eat # 然后调用

# 尝试删除属性方法
# del d.eat # 会报错

# 如果需要删除属性方法，再写一个方法
# del d.eat
# d.eat





























