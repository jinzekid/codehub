# Author: Jason Lu
import sqlalchemy
from sqlalchemy import create_engine, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:@localhost/oldboydb",
                       encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类

class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "<%s name:%s>" %(self.id, self.name)

class StudyRecord(Base):
    __tablename__ = 'study_record'  # 表名
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey('student.id'), nullable=False)

    student = relationship("Student", backref="my_study_record")

    def __repr__(self):
        return "<%s status: %s;day: %s>" %(self.student.name, self.status, self.day)


Base.metadata.create_all(engine)  # 创建表结构
#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)
Session = Session_class() #生成session实例

# 创建学员，插入数据操作
user_obj = Student(name="alex", register_date="2017-10-23")  # 生成你要创建的数据对象
user_obj2 = Student(name="jason", register_date="2017-11-30")  # 生成你要创建的数据对象
user_obj3 = Student(name="Rain", register_date="2015-04-20")  # 生成你要创建的数据对象
user_obj4 = Student(name="Eric", register_date="2016-07-10")  # 生成你要创建的数据对象

# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj2)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj3)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj4)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add_all([user_obj, user_obj2, user_obj3, user_obj4])

study_obj1 = StudyRecord(day=1, status="YES", stu_id=1)
study_obj2 = StudyRecord(day=2, status="YES", stu_id=1)
study_obj3 = StudyRecord(day=3, status="YES", stu_id=1)
study_obj4 = StudyRecord(day=1, status="YES", stu_id=2)

# Session.add_all([study_obj1, study_obj2, study_obj3, study_obj4])
# Session.commit()  # 现此才统一提交，创建数据

stu_obj = Session.query(Student).filter(Student.name=="alex").first()
print(stu_obj.my_study_record)

