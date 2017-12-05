# Author: Jason Lu
import time

def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

'''
c = consumer("Jason")
c.__next__() # 只是唤醒
c.send("hahaha") # 是唤醒同时穿值
'''

# 单线程下的并行效果
def producer(name):
    c = consumer('A') # 第一步：生成 生成器
    c2 = consumer('B')
    c.__next__() # 第二步：才会继续往下走，调用yield，接着返回，等待send
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i) # 做完后分别送给消费者
        c2.send(i)

producer("alex")


