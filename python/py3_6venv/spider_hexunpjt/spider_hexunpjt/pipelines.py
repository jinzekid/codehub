# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class SpiderHexunpjtPipeline(object):

    def __init__(self):
        # 连接数据库
        print(">>>init pipeline<<<")
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='',
                                    db='hexun')
        # 通过cursor创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 每一篇博文列表页中包含多篇博文的信息，可以通过for循环一次处理各博文的信息
        print(">>>process_item<<<")
        int_len = len(item["name"])
        for j in range(0, int_len):
            name = item['name'][j]
            url  = item['url'][j]
            hits = item['hits'][j]
            comment = item['comment'][j]

            # 构造sql语句
            sql = "insert into myehxun(name, url, hits, comment) values(" \
                  "'"+name+"','"+url+"','"+hits+"','"+comment+"')"
            print(sql)
            # 通过query实现执行对应的sql语句
            self.cursor.execute(sql)

        self.conn.commit()
        return item

    def close_spider(self, spider):
        # 关闭数据库连接
        print(">>>close spider<<<")
        self.cursor.close()
        self.conn.close()