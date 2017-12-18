# Author: Jason Lu

class Role(object):

    n = "ttt"

    # 构造函数
    def __init__(self, name, role, weapon, life_value=100, money=15000, private_life = 200):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        # 私有属性
        self.__private_life = private_life

    def show_private_life(self):
        print("%s private life is: %s" %(self.name, self.__private_life))

    # 私有方法
    def __do_private_method(self):
        print("this is private method...")

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)

    # 析构函数
    def __del__(self):
        print("%s 彻底死了...%s" %(self.name, self.role))

r1 = Role('Alex', 'police', 'AK47') #生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色

r1.got_shot()
# 实例变量
r1.bullet_prove = True
r1.n = "改类变量"
print("r1:", r1.n) #r1: 改类变量
print("r2:", r2.n) #r2: ttt
print(Role.n) #ttt

# 手动析构（不一定被自动销毁，根据系统）
# del r1

# 访问私有属性可以定义方法
r1.show_private_life()
