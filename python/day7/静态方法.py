# Author: Jason Lu

class Dog(object):

    def __init__(self, name):
        self.name = name

    @staticmethod # 静态方法跟类没什么关系了
    def eat():
        print("%s is eating %s" % ('dddd', 'dd'))

######################################################
d = Dog("dog")
d.eat() #output: dddd is eating dd



































