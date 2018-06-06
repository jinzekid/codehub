# -*- encoding:utf-8 -*-
import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud

jieba.add_word('美国留学')
jieba.add_word('面试')

content = open('testing.txt', 'r', encoding='utf-8').read()
words_ls = jieba.cut(content, cut_all=True)
words_split = " ".join(words_ls)

#print(words_split)

wc = WordCloud()
wc.font_path = "/System/Library/Fonts/STHeiti Medium.ttc"
my_wordcloud = wc.generate(words_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

wc.to_file('zzz.png')




