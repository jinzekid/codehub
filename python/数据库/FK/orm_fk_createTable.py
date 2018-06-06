# Author: Jason Lu
import sqlalchemy
from sqlalchemy import create_engine, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:@localhost/oldboydb",
                       encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(256))
    city = Column(String(128))
    state = Column(String(128))

    def __repr__(self):
        return "street:{} city:{} state:{}".format(self.street, self.city, self.state)

Base.metadata.create_all(engine)  # 创建表结构







