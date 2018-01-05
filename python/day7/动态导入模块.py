# Author: Jason Lu

# 方法一
'''
import day7.lib.aa as a
objc = a.C()
print(objc)
'''

# 方法二
'''
modname = "day7.lib.aa"
mod = __import__(modname) # 导入到day7层级
cls_c = mod.lib.aa.C
print(mod.lib.aa)
print(mod.lib.aa.C)
objc = cls_c()
print(objc)
'''

# 方法三
# 官方建议
import importlib
aa = importlib.import_module("day7.lib.aa")
objc = aa.C()
print(objc)
