# Author: Jason Lu

'''
# 方法一
# 把模块中的say_hello方法引入进来
from day5.module_test.module_1 import say_hello

say_hello()

'''

'''
# 方法二
# 如果有重复名称的方法可以使用别名来代替
# from day5.module_test.module_1 import say_hello as say_hello_inModule

def say_hello():
    print("func in main")
    
say_hello()
say_hello_inModule()

'''

'''
# 方法三
import day5.module_test.module_1

day5.module_test.module_1.say_hello()

'''

'''
# 方法四
# 导入包的本质就是执行该包下的__init__.py文件
输出：from the package package_test

import day5.package_day5

'''

import sys, os
print(sys.path)

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, path)
sys.path.append(path)
print(sys.path)

# 写法一 把文件中所有的代码都引入进来
# import module_test
# module_test.func_module_test()

# 写法二 只把func_module_test引入进来，相当于这个方法直接引入进来
from module_test import func_module_test
func_module_test()