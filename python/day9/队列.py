# Author: Jason Lu

import queue

'''
# q = queue.Queue() # 先进先出
q = queue.LifoQueue() # 后进先出
q.put("d2")
q.put("d3")

print(q.qsize())
print(q.get())
print(q.get(timeout=10))
'''

q = queue.PriorityQueue()
q.put((10, "jason"))
q.put((-1, "eson22"))
q.put((3, "eson"))
q.put((6, "jason22"))

print(q.get())
print(q.get())
print(q.get())
print(q.get())











