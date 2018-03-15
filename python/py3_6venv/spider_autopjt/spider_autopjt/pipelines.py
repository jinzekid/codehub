# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class SpiderAutopjtPipeline(object):

    def __init__(self):
        print("init_spider")
        self.file = codecs.open('mydata.json', 'wb', encoding='utf-8')

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
        return item

    # close_spider() 方法一般在关闭蜘蛛时调用
    def close_spider(self, spider):
        print("close_spider")
        self.file.close()
