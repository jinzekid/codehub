'''
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class SpiderMypjtPipeline(object):

    def __init__(self):
        # 首先以写入的方式创建或打开一个普通文件用于存储爬取到的数据
        self.file = codecs.open('mydata2.txt', 'wb', encoding='utf-8')

    # process_item 为pipelines中主要处理方法，默认会自动调用
    def process_item(self, item, spider):
        # 设置每行要写的内容
        l = str(item) + '\n'
        print(l)

        # 将对应信息写入文件中
        self.file.write(l)
        return item

    # close_spider() 方法一般在关闭蜘蛛时调用
    def close_spider(self, spider):
        self.file.close()
'''

import codecs
import json

class SpiderMypjtPipeline(object):
    def __init__(self):
        print("init pipeline")
        self.file = codecs.open('mydata2.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        print("process_item: %s" % item)
        # 通过dict(item)将item转化成一个字典
        # 然后通过json模块的dumps()处理字典数据
        try:
            i = json.dumps(dict(item), ensure_ascii=False)
            print("i: %s" % i)
            line = i+'\n'
            print(line)

            # 将对应信息写入文件中
            self.file.write(line)
        except Exception as e:
            print(e)

        return item


    # close_spider() 方法一般在关闭蜘蛛时调用
    def close_spider(self, spider):
        print("close_spider")
        self.file.close()
