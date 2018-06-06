# Author: Jason Lu

import threading
import time

event = threading.Event()
event.set() # 先设置标志位

def lighter():
    count = 0
    while True:
        if count > 10: # 改成红灯
            event.set()  # 设置标志位，变绿灯
            # print(">>改成绿灯了...")
            count = 0
        elif count > 5:
            event.clear()  # 清空标志位
            print("\033[41;1m改成红灯了...\033[0m")
        else:
            print('\033[42;1m--green light on---\033[0m')

        time.sleep(1)
        count += 1

# 需要不断的检测红绿灯
def car(name):

    while True:
        if event.is_set(): # 判断是否设置标志位
            print("[%s] running..." %name)
            time.sleep(1)
        else:
            print("[%s]sees red light, waiting..." %name)
            event.wait()
            print("[%s]green light is on, start going..." %name)


light1 = threading.Thread(target=lighter, args=[])
light1.start()

car1 = threading.Thread(target=car, args=("Tesla",))
car1.start()



