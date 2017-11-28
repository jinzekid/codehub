# Author: Jason Lu

school = "oldboy edu."

def change_name(name):
    global school # 修改全局变量， 不建议用（因为是全局变量）
    school = "Mage Linux"
    print(school)

change_name("aaa")
print(school)


# 不建议这么做
def change_name2():
    global name
    name = "alex"

change_name2()
print(name)

# 列表，字典，集合, 可以修改
names = ["aaa", "bbb", "ccc"]
def change_name3():
    names[0] = "kkk"
    print("in func: ", names) #output：['kkk', 'bbb', 'ccc']

change_name3()
print(names) #output：['kkk', 'bbb', 'ccc']