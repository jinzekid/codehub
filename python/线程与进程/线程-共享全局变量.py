# Author: Jason Lu
import threading

threads = []

def work(count):
    for i in range(count):
        print('[%s] => %s' %(threading.current_thread(), count))


for i in range(5):
    t = threading.Thread(target=work, args=(i, ))
    t.start()


