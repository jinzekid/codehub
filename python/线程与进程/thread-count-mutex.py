# Author: Jason Lu
import _thread as thread, time

mutex = thread.allocate_lock()

def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        mutex.acquire()
        print('[%s] => %s' % (myId, i))
        mutex.release()

threads = []
for i in range(5):
    threads.append(thread.start_new_thread(counter, (i, 5)))

time.sleep(6)

for thread in threads:
    print('>>:thread id: %s' % thread)


print('main thread exiting.')
