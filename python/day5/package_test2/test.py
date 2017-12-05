# Author: Jason Lu

from day5.module_test import func_test as func1

def logger():
    func1()
    print("in the logger")


def search():
    func1()
    print("in the search")

logger()
search()