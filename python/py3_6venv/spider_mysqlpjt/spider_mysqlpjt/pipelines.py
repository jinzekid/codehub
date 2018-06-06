# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class SpiderMysqlpjtPipeline(object):

    def __init__(self):
        print(">>>init_spider")
        # 刚开始时连接对应的数据库
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='',
                                    db='mypydb')

    def process_item(self, item, spider):
        name = item['name'][0]
        keywd = item['keywd'][0]

        # 构造对应的sql语句
        sql = "insert into mytb(title, keywd) " \
              "values('"+name+"','"+keywd+"')"

        print("=====执行sql语句=====")
        print(sql)
        # 通过query实现执行对应的sql语句
        affect_rows = self.conn.query(sql)
        print("影响 "+affect_rows+' 行')
        return item

    def close_spider(self, spider):
        print(">>>close_spider")
        self.conn.close()
