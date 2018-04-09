import jieba
import jieba.analyse


with open('testing.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    seg_list = jieba.cut(content)
    print("[精确模式]: ", '/ '.join(seg_list))

    tas = jieba.analyse.extract_tags(content, topK=5)
    print("[关键词]: ", ' / '.join(tags)) 

