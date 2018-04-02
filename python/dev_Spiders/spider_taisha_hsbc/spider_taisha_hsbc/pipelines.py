# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class SpiderTaishaHsbcPipeline(object):
    def process_item(self, item, spider):
        print(">>>process_item<<<")
        int_len = len(item["name"])
        print("板块总数: {}".format(int_len))
        print("=========================")

        list_name = []
        list_topic = []
        list_note = []
        for j in range(0, int_len):
            name = item['name'][j]
            topic_d = item['topic_d'][j]
            topic = self.parse_revise_data(topic_d)
            note_d = item['note_d'][j]
            note = self.parse_revise_data(note_d)

            # note = item['note'][j]

            print("板块名称:%s" % name)
            print("主题数量:%s" % topic)
            print("帖子数量:%s" % note)
            print("=========================")
            list_name.append(name)
            list_topic.append(topic)
            list_note.append(note)

        print("=======")
        print("{} {} {}".format(list_name, list_topic, list_note))
        return item

    def close_spider(self, spider):
        print(">>>close_spider<<<")
        pass

    def parse_revise_data(self, str_topic_note):
        # 可以正确解析
        pat = '.*?: (.*?)</em>.*?'
        pat_sub = '<span title="(.*?)">.*?'
        list_topic = re.compile(pat).findall(str(str_topic_note))
        tmp_topic = []
        for item in list_topic:
            list_topic_sub = re.compile(pat_sub).findall(item)
            if len(list_topic_sub) > 0:
                tmp_topic = list_topic_sub[0]
            else:
                tmp_topic = item

        return tmp_topic

    def parse_data_barchar(self, list_name, list_topic, list_note):
        import numpy as np
        import matplotlib as mpl
        mpl.use('TkAgg')
        import matplotlib.pyplot as plt

        mpl.rcParams['axes.titlesize'] = 20
        mpl.rcParams['xtick.labelsize'] = 16
        mpl.rcParams['ytick.labelsize'] = 16
        mpl.rcParams['axes.labelsize'] = 16
        mpl.rcParams['xtick.major.size'] = 0
        mpl.rcParams['ytick.major.size'] = 0

        # 包含了狗，猫和猎豹的最高奔跑速度，还有对应的可视化颜色
        speed_map = {
            'dog': (48, '#7199cf'),
            'cat': (45, '#4fc4aa'),
            'cheetah': (120, '#e1a7a2')
        }
        pass

