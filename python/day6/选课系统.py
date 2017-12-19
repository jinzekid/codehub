# Author: Jason Lu
# 选课系统

##################################################
class School(object):

    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.__city = city
        self.students = []
        self.staffs = []

    def tell(self):
        print('''---info of School---
        Name: %s
        City: %s
        Address: %s
        Students: %s
        Staffs: %s''' %(self.name, self.__city, self.address, self.students, self.staffs))

    # 注册方法
    def enroll(self, stu_obj):
        print("为学生%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        print("雇佣新员工：%s" % staff_obj.name)
        self.staffs.append(staff_obj)

##################################################
class Course(object):

    def __init__(self, name, price, outline):
        self.name = name
        self.price = price
        self.__course_outline = outline

    def print_course_outline(self):
        print("%s outline: %s" %(self.name, self.__course_outline))

##################################################
class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

##################################################
class Teacher(object):

    def __init__(self, name):
        self.name = name

##################################################
class Classes(object):

    def __init__(self, name, semester, start_time, course_name, teacher):
        self.name = name
        self.start_time = start_time
        self.semester = semester
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

##################################################
class ClassRecord(object):

    def __init__(self, class_name, count, class_date):
        self.class_name = class_name
        self.count = count
        self.class_date = class_date

##################################################
class StudyRecord(object):

    def __init__(self, study_record, sign_status, sign_date, point):
        self.study_record = study_record
        self.sign_status = sign_status
        self.sign_date = sign_date
        self.point = point

##################################################

def print_list(list_content):
    # 打印系统菜单
    for v in list_content:
        print(v)


##################################################

list_school = []

list_sys_menu = ["1.系统管理员", "2.我是老师", "3.我是学生"]
list_admin_menu = ["1.选择学校", "2.创建学校", "Q/q:返回上级菜单"]
list_school_menu = ["1.创建班级", "2.创建讲师", "3.创建课程"]

while True:
    print("欢迎进入选择系统:))))")

    # 打印系统菜单
    print_list(list_sys_menu)

    val = int(input("请选择您的权限："))
    if val == 1:

        while True:
            # print("我是系统管理员")
            # 打印管理员菜单
            print_list(list_admin_menu)

            admin_code = input("请选择您的操作：")

            if admin_code == 'Q' or admin_code == 'q':
                break
            else:
                if admin_code == 1:
                    # 打印所有现存的学校
                    pass
                else:
                    # 开始创建学校
                    str_school_name = input("请输入学校名字:")
                    str_school_address = input("请输入学校地址:")
                    str_school_city = input("请输入学校所在城市:")

                    school = School(str_school_name, str_school_address, str_school_city)

                    list_school.append(school)
                    print("==============学校创建完成==============")



    elif val == 2:
        print("我是老师")
    else:
        print("我是学生")

























