# Author: Jason Lu

import pymysql
# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', passwd='', db='oldboydb')
# 创建游标
cursor = conn.cursor()
# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from student")
print(cursor.fetchmany(2))
print(cursor.fetchone())
print(cursor.fetchone())
print()
print(effect_row)
print()
print(cursor.fetchall())

data = [
    ('n1', 20, '2015-05-04', 'F'),
    ('n2', 30, '2015-06-04', 'F'),
]
# 默认开启事物
cursor.executemany("insert into student "
                   "(name, age, register_date, sex) "
                   "values(%s,%s,%s,%s)", data)
# 需要commit操作
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()


