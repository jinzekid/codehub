# Author: Jason Lu

def bulk(self):
    print("%s is yelling..." %(self.name))

class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s is eating..." %(self.name))


d = Dog("alex")
choice = input(">>>:").strip()

if hasattr(d, choice):
    func = getattr(d, choice)
    func()
else:
    pass
    # 通过字符串动态装配方法
    '''
    setattr(d, choice, bulk)
    d.talk(d)
    '''
    # 通过字符串动态装配属性
    '''
    setattr(d, choice, 22)
    print(getattr(d, choice))
    '''

# 判断一个对象里是否有对应的字符串的方法
print(hasattr(d, choice))
# 根据字符串去获取obj对象里的对应的方法的内存地址
print(getattr(d, choice))

# 删除对象属性或者方法
print("will del func: %s" %(choice))
delattr(d, choice)
print(hasattr(d, choice))