# Author: Jason Lu
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost/oldboydb",
                       encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类

class User(Base):
    __tablename__ = 'stu'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s>" %(self.id, self.name)


Base.metadata.create_all(engine)  # 创建表结构

#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)
Session = Session_class() #生成session实例

# 插入数据操作
'''
user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
user_obj2 = User(name="jason", password="12345")  # 生成你要创建的数据对象

print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
Session.add(user_obj2)  # 把要创建的数据对象添加到这个session里， 一会统一创建

print(user_obj.name, user_obj.id)  # 此时也依然还没创建
Session.commit()  # 现此才统一提交，创建数据

'''

# 查询数据
'''
data = Session.query(User).filter_by(name="alex").all()
print(data[0].name, data[0].password)

data = Session.query(User).filter_by().all()
print(data)

data_user = Session.query(User).filter(User.id > 1).first()
print(data_user)
# 修改数据
data_user.name = 'Jason Lu'
Session.commit()
'''

'''
my_user = Session.query(User).filter(User.id > 1).first()
my_user = "Jack"

fake_user = User(name='Rain', password='12345')
Session.add(fake_user)

print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all() )  #这时看session里有你刚添加和修改的数据

Session.rollback() #此时你rollback一下
'''

# 统计
cnt = Session.query(User).filter(User.name.like("al%")).count()
print(cnt)

# 分组
from sqlalchemy import func
print(Session.query(func.count(User.name), User.name).group_by(User.name).all())
# 原生sql语句
# SELECT count(user.name) AS count_1, user.name AS user_name
# FROM user GROUP BY user.name




# 创建表方法二
'''
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper

metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(12))
             )


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password


mapper(User, user)  # the table metadata is created separately with the Table construct, then associated with the User class via the mapper() function
'''







