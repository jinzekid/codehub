# Author: Jason Lu
import orm_fk_createTable
from sqlalchemy.orm import sessionmaker, relationship

#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=orm_fk_createTable.engine)
Session = Session_class() #生成session实例

# addr1 = orm_fk_createTable.Address(street="jinganshi", city="shanghai", state="SH")
# addr2 = orm_fk_createTable.Address(street="huangpu", city="huangpinanlu", state="SH")
# addr3 = orm_fk_createTable.Address(street="Yanjiao", city="LangFang", state="HB")
# addr4 = orm_fk_createTable.Address(street="Wudaokou", city="Haidin", state="BJ")
#
# # Session.add_all([addr1, addr2, addr3, addr4])
#
# c1 = orm_fk_createTable.Customer(name="Alex", billing_address=addr1, shipping_address=addr2)
# c2 = orm_fk_createTable.Customer(name="Jason", billing_address=addr3, shipping_address=addr3)
#
# Session.add_all([c1, c2])
# Session.commit()

obj = Session.query(orm_fk_createTable.Customer).filter(orm_fk_createTable.Customer.name=="Alex").first()
print(obj.name, obj.billing_address, obj.shipping_address)

def main():
    print("main()")


if __name__ == '__main__':
    main()

