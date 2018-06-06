# Author: Jason Lu

import gevent
import time

def func1():
    print("start func1...")
    time.sleep(2)
    print("func1 done....")

def func2():
    print("start func2...")
    time.sleep(1)
    print("func2 done...")

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2)
])





