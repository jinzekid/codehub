# Author: Jason Lu

import os, sys

# 写法一
# import test1 #加载所有test1的代码，赋值给test1='test1.py all code'

# 写法二 从当前目录导入test
from . import test1

print("package_test init ", __file__)