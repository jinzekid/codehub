# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request

class SpiderQtpjtPipeline(object):

    def process_item(self, item, spider):
        print(">>>process_item<<<")
        # 一个图片列表中有多张图片，通过for循环依次将图片存储到本地
        print("长度：" + str(len(item["picurl"])))
        for i in range(0, len(item["picurl"])):
            thispic = item["picurl"][i]
            trueurl = thispic + ".jpg"
            print(trueurl)
            localpath = "pic/"+item["picid"][i]+".jpg"
            print(localpath)
            try:
                urllib.request.urlretrieve(trueurl, filename=localpath)
            except urllib.error.URLError as e:
                if hasattr(e, 'code'):
                    print(e.code)
                if hasattr(e, 'reason'):
                    print(e.reason)
        return item
