# Author: Jason Lu

import multiprocessing
import time

def run(name):
    time.sleep(2)
    print("hello", name)

p = multiprocessing.Process(target=run, args=('bob',))
p.start()
p.join()

