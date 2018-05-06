#!/Users/jasonlu/.virtualenvs/pyven3_6/bin/python
import jieba
import jieba.analyse
from scipy.misc import imread
import numpy as np
from pandas import DataFrame, Series
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


myfont = FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc')
mpl.rcParams['axes.unicode_minus'] = False

stopwords_path = 'stop_words.txt' #停用词词表

jieba.add_word('美国留学')
jieba.add_word('面试')

with open('testing_南极洲留学.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    #seg_list = jieba.cut(content, cut_all=False)
    #print("[精确模式]: ", '/ '.join(seg_list))

    #seg_list = jieba.cut(content, cut_all=True)
    #print("[全模式]: ", '/ '.join(seg_list))

    #seg_list3 = jieba.cut_for_search(content)
    #print("[搜索引擎模式]: " , ' \ '.join(seg_list3))

    tags = jieba.analyse.extract_tags(content, topK=10)
    print("[关键词]:", ' \ '.join(tags))

#    tags = jieba.analyse.extract_tags(content, topK=10, withWeight=True, allowPOS=('n','nr','ns'))
    list_kw = []
    list_vl = []

    tags = jieba.analyse.extract_tags(content, topK=10, withWeight=True, allowPOS=())
    for item in tags:
        list_kw.append(item[0])
        list_vl.append(item[1])
        print(item[0], item[1])

    ax = plt.gca()
    plt.bar(range(len(list_vl)), list_vl, color='rgb', tick_label=list_kw)
    plt.title('中文',fontproperties=myfont)
    ax = plt.gca()
    ax.set_xticklabels(list_kw, fontproperties=myfont, rotation='horizontal')
    plt.show()

"""
    fig = plt.figure()
    x = Series(list_vl, index=list_kw)
    x.plot(kind='bar',color='r',alpha=0.7)

    ax = plt.gca()
    ax.set_xticklabels(list_kw, fontproperties=myfont, rotation='horizontal')

    fig.tight_layout()
    plt.title('中文',fontproperties=myfont)
    plt.show()
"""



