"""
使用multiprocessing起始新程序，不论os.fork是否可用
"""
import os
from multiprocessing import Process

def run_program(arg):
    os.execlp('python', 'python', 'child.py', str(arg))

if __name__ == '__main__':
    for i in range(5):
        Process(target=run_program, args=(i,)).start()

    print('parent exit')
