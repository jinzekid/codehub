# Author: Jason Lu
# 都用新式类写法

class School(object):

    # 构造函数
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    # 注册方法
    def enroll(self, stu_obj):
        print("为学生%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        print("雇佣新员工：%s" % staff_obj.name)
        self.staffs.append(staff_obj)

class SchoolMember(object):

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class Teacher(SchoolMember):

    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''---info of Teacher:%s---
                Name:%s
                Age:%s
                Sex:%s
                Salary:%s
                Course:%s''' %(self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching course: [%s]" %(self.name, self.course))


class Student(SchoolMember):

    def __init__(self, name, age, sex, stu_id, grade, courses):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade
        self.courses = courses

    def tell(self):
        print('''---info of Student:%s---
                Name:%s
                Age:%s
                Sex:%s
                Stu_id:%s
                Grade:%s
                Courses:%s''' %(self.name, self.name, self.age, self.sex, self.stu_id, self.grade, self.courses))

    def pay_tuition(self, amount):
        print("%s has paid tuition: %s" %(self.name, amount))

############################################
school = School("高级中学", "上海市静安区xxx路xxx号")

t1 = Teacher("t1", 30, "男", 2000, "Python")
t2 = Teacher("t2", 22, "M", 300, "Linux")

s1 = Student("s1", 18, "女", 12, "一年级", "python")
s2 = Student("s2", 22, "女", 16, "一年级", "Linux")


t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.students)
print(school.staffs)

school.staffs[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)










