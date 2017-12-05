# Author: Jason Lu

import sys, os

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 添加路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from day5 import package_test as tt
tt.test1.func_print()

from day5 import package_test
package_test.test1.func_print()





