# Author: Jason Lu

import os
import sys

print(__file__)  # 相对路径
print((os.path.abspath(__file__)))  # 绝对路径
print(os.path.dirname(os.path.abspath(__file__)))  # 找到当前路径
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 找到父亲路径

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

main.run()
# settings.setting()
