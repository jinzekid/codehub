# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderJdPhonePipeline(object):
    def process_item(self, item, spider):
        print(">>>process_item<<<")

        int_len = len(item["price"])
        for j in range(0, int_len):
            price = item['price'][j]
            name = item['name'][j]
            print("name:%s" %name)
            print("price:%s" %price)
            print("=========================")
        return item

    def close_spider(self, spider):
        print(">>>close_spider<<<")
        pass