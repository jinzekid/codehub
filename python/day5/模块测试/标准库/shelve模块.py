# Author: Jason Lu
# 持久化数据
import shelve, datetime

d = shelve.open("shelve_test")
# 读取数据
print(d.get("name"))
print(d.get("info"))
print(d.get("date"))
d.close()

# info = {"age": 22, "job": "it"}
# name = ["alex", "rain", "test"]
# d["name"] = name # 持久化列表
# d["info"] = info # 持久dict
# d["date"] = datetime.datetime.now()
# d.close()


