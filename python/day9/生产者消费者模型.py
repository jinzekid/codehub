# Author: Jason Lu

import threading, time
import queue

q = queue.Queue(maxsize=10)

def Producer(name):
    i = 1
    while True:
        q.put("骨头: %s" % (i))
        print("生产了骨头", i)
        i += 1
        time.sleep(0.5)


def Consumer(name):
    # while q.qsize() > 0:
    while True:
        print("[%s] 取到[%s], 并且吃了它..." %(name, q.get()))
        time.sleep(1)

t_producer = threading.Thread(target=Producer, args=("Jason", ))
t_consumer = threading.Thread(target=Consumer, args=("test", ))
t_consumer22 = threading.Thread(target=Consumer, args=("test22", ))

t_producer.start()
t_consumer.start()
t_consumer22.start()

