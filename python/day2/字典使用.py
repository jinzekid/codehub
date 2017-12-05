# Author: Jason Lu

# 字典操作
print("\n============字典操作============\n")
info = {
    'stu1101': "1111",
    "stu1102": "2222",
    "stu1103": "3333"
}

print(info["stu1101"])
info["stu1101"] = "1000" #存在修改
print(info)
info["stu1104"] = "4444" #不存在增加
print(info)

# del
del info["stu1101"] #删除元素
print(info)

# pop
info.pop("stu1102")
print(info)

# 查找
# info["stu1105"]
print(info.get("stu1105")) #安全获取方法使用get
if info.get("stu1105") == None:
    print("none of value")

print("stu1104" in info) #info.has_key("1103") in py2.x
if "stu1104" in info:
    print("has key value")


# 多级字典的嵌套
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"
print(av_catalog["大陆"]["1024"])
#ouput ['全部免费,真好,好人一生平安', '服务器在国外,慢,可以用爬虫爬下来']
av_catalog["大陆"]["1024"][1] = "可以在大陆做镜像"
print(av_catalog.values()) #打印所有value值
av_catalog.setdefault("大陆2", {"www.baidu.com":[1,2]}) #查找如果没有大陆2就直接插入数据
print(av_catalog.values()) #打印所有value值

b = {
    "stu1101": "324",
    "1":"111",
    "2":"222"
}
av_catalog.update(b) #合并字典
print(av_catalog)

c = dict.fromkeys([6, 7, 8], "debug") #初始化一个新的字典
print(c)

# 注意类似浅拷贝的问题，其实{"name":"alex"}共享一个引用
c = dict.fromkeys([6,7,8], [1, {"name":"alex"}, 444]) #初始化一个新的字典
print(c)
c[7][1]["name"] = "Jason"
print(c)

# 字典循环
print("\n============字典循环============\n")

# 更高效
for i in info:
    print("tt:", i, info[i])

print("\n========================\n")


# 有个字典把列表的过程，效率低下
for k, v in info.items():
    print(k, v)

print("\n============end of 字典操作============\n")
