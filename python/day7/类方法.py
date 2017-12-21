# Author: Jason Lu

class Dog(object):
    # 类变量
    # n = 333
    name = "ahaha"

    def __init__(self, name):
        self.name = name

    @classmethod # 静态方法跟类没什么关系了
    def eat(self):
        print("%s is eating %s" % (self.name, 'dd'))


    def talk(self):
        print("%s is talking.." %self.name)

######################################################
d = Dog("dog")
d.eat()



































