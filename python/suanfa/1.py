from datetime import datetime
from timeit import timeit as tt
t2 = tt('x=range(100)')
print(t2)

from random import randrange
L = [randrange(10000) for i in range(100000)]
S = set(L)

start = datetime.now()
r_l = 42 in L 
print(r_l)
delta = datetime.now() - start
print("List delta:", delta.microseconds)

start = datetime.now()
r_l = 42 in S 
print(r_l)
delta = datetime.now() - start
print("Set delta:", delta.microseconds)


def func_set():
    r_s = 42 in S
    print(r_s)


def func_list():
    r_l = 42 in L
    print(r_l)
def calu_func_time(func):
    start = datetime.now()
    func()
    delta = datetime.now() - start
    print(func , ":elapsed time in microseconds:" , delta.microseconds)


def calu_func_time(func):
    start = datetime.now()
    func()
    delta = datetime.now() - start
    print(func , ":elapsed time in microseconds:" , delta.microseconds)

calu_func_time(func_list)
calu_func_time(func_set)

import os
#import cProfile
#cProfile.run('test1()')
#cProfile.run('test2()')

