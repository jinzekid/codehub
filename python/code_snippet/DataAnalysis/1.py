# -*- encoding:utf-8 -*-
import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

list_test = [1,2,3,4,5]
for i in list_test:
    print(i)


if __name__ == "__main__":

    mpl.rcParams['font.sans-serif'] = ['FangSong']
    #mpl.rcParams['axes.unicode_minus'] = False

    content = open("testing.txt","rb").read()

    # tags extraction based on TF-IDF algorithm
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
    text =" ".join(tags)
    #text = unicode(text)
    # read the mask
    d = path.dirname(__file__)
    trump_coloring = imread(path.join(d, "Trump.jpg"))

    wc = WordCloud(font_path='simsun.ttc',
            background_color="white", max_words=300, mask=trump_coloring,
            max_font_size=40, random_state=42)

    # generate word cloud
    wc.generate(text)

    # generate color from image
    image_colors = ImageColorGenerator(trump_coloring)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()

