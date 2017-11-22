# Author: Jason Lu

# 带缓冲flush的作用

import sys
import time

for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)