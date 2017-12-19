# Author: Jason Lu
# 经典类和新式类主要区别在于继承上
######################################################
class Animal:
    def __init__(self):
        pass

# class People：经典类
class People(object): # 新式类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s eating..." % self.name)

    def sleep(self):
        print("%s sleeping..." % self.name)

    def __del__(self):
        print("%s destory...." % (self))

class Relation(object):
    def make_friends(self, obj):
        print("%s is making friends with %s" % (self.name, obj.name))

######################################################
# 继承了People
class Man(People, Relation):

    # 重构构造函数
    def __init__(self, name, age, money):
        # 调用父类方法一，不适合多继承，经典类写法
        # People.__init__(self, name, age)
        # Animal.__init__(self, name, age)

        # 调用父类方法二，适合多继承，只要写一遍
        super(Man, self).__init__(name, age) # 新式类写法


        self.money = money
        pass

    def sleep(self):
        # People.sleep(self)
        print("%s sleeping..." % self.name)

# 继承了People
class Woman(People):

    def get_birth(self):
        print("%s is born a baby..." % self.name)

######################################################
p = People("tt", 23)
m = Man("m1", 33, 100)
m.eat() # m1 eating...
print(m.money) # 100
m.sleep() # m1 sleeping...
w = Woman("w1", 26)
w.get_birth() # w1 is born a baby...
m.make_friends(w) # m1 is making friends with w1