# Author: Jason Lu
import gevent

def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m')
    gevent.sleep(2)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')


gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    # gevent.spawn(func3),
])

# from gevent import monkey
# monkey.patch_all()
# import gevent
# from gevent import Greenlet
#
# class Task(Greenlet):
#     def __init__(self, name):
#         Greenlet.__init__(self)
#         self.name = name
#     def _run(self):
#         print("Task %s: some task..." %(self.name))
#
# t1 = Task("task1")
# t2 = Task("task2")
# t1.start()
# t2.start()
# # here we are waiting all tasks
# gevent.joinall([t1, t2])