import jieba
import jieba.analyse

content = open('testing.txt', 'rb').read()

keywords = jieba.analyse.extract_tags(content, topK=10, withWeight=True, allowPOS=('n','nr','ns'))

for item in keywords:
    print(item[0], item[1])

print("=====")

#seg_list = jieba.cut(content, cut_all=False)
#print("Full mode: "  + ",".join(seg_list))




