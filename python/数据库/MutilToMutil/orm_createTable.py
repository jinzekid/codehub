# Author: Jason Lu
import sqlalchemy
from sqlalchemy import create_engine, DATE, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

# 添加中文方式?charset=utf8
engine = create_engine("mysql+pymysql://root:@localhost/oldboydb?charset=utf8",
                       encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类

# 自动维护，不需要用户关心
book_author = Table('book_author', Base.metadata,
                    Column('book_id', Integer, ForeignKey('book.id')),
                    Column('author_id', Integer, ForeignKey('author.id')))

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    pub_date = Column(DATE)
    authors = relationship("Author", secondary=book_author, backref='book')

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def __repr__(self):
        return self.name

# class BookAuthor(Base):
#     __tablename__ = 'book_author'
#     id = Column(Integer, primary_key=True)
#
#     author_id = Column(Integer, ForeignKey("author.id"))
#     book_id = Column(Integer, ForeignKey("book.id"))
#
#     def __repr__(self):
#         return "name:{} author:{}".format(self.name, self.author_id)


Base.metadata.create_all(engine)  # 创建表结构







