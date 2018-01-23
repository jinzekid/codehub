# Author: Jason Lu
import orm_createTable
from sqlalchemy.orm import sessionmaker, relationship

#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=orm_createTable.engine)
Session = Session_class() #生成session实例

# b1 = orm_createTable.Book(name="Learn python with Alex", pub_date='2014-05-02')
# b2 = orm_createTable.Book(name="Learn java with Jason", pub_date='2016-08-02')
b3 = orm_createTable.Book(name="跟我学开车", pub_date='2017-10-02')
#
#
a1 = orm_createTable.Author(name="Alex")
# a2 = orm_createTable.Author(name="Jason")
# a3 = orm_createTable.Author(name="BBB")
#
# b1.authors = [a1, a2]
# b3.authors = [a1, a2, a3]
#
# Session.add_all([b1, b2, b3, a1, a2, a3])
b3.authors = [a1]
Session.add_all([b3])
Session.commit()


# data = Session.query(orm_createTable.Author).filter(orm_createTable.Author.name=='Alex').first()
# print(data.book)
# # print(data.book[1].pub_date)
# print()
# book_obj = Session.query(orm_createTable.Book).filter(orm_createTable.Book.id==2).first()
# print(book_obj.authors)



