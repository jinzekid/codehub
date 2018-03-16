# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import pymysql

class SpiderAutopjtPipeline(object):

    def __init__(self):
        print("init_spider")
        self.file = codecs.open('mydata.json', 'wb', encoding='utf-8')
        print("init_database")
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='',
                                 db='mypydb')
        # 通过cursor创建游标
        self.cursor = self.conn.cursor()

        print("end init")

    def process_item(self, item, spider):
        print("processing...")
        for j in range(0, len(item['name'])):
            name = item['name'][j]
            price = item['price'][j]
            link = item['link'][j]
            comnum = item['comnum'][j]

            goods = {'name':name, 'price':price, 'comnum':comnum, 'link':link}

            i = json.dumps(dict(goods), ensure_ascii=False)
            line = i + '\n'
            self.file.write(line)


            # 保存数据库
            # 构造对应的sql语句
            sql = "insert into mydangdangtb(name, price, link, comnum) " \
                  "values" \
                  "('" + name + "','" + price + "','"+ link + "'," \
                                                              "'" +comnum+"');"
            print("=====执行sql语句=====")
            print(sql)

            self.cursor.execute(sql)
            # # 通过query实现执行对应的sql语句
            # affect_rows = self.conn.query(sql)
            # print("影响 " + affect_rows + ' 行')
        self.conn.commit()
        return item

    # close_spider() 方法一般在关闭蜘蛛时调用
    def close_spider(self, spider):
        print("close_spider")
        self.file.close()
        self.cursor.close()
        self.conn.close()

