#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python 
import sys 
sys.path.append('/Users/jasonlu/Desktop/Dev/GitHub/codehub/python/code_snippet/test')

   
func1()

def func_before(*args, **kwargs):
    print('func_before...')

def func_after(*args, **kwargs):
    print('func_after...')

def func_filter(before_func, after_func):
    def outer(main_func):
        def wrapper(*args, **kwargs):
            before_result = before_func(*args, **kwargs)
            if before_result is not None:
                return before_result

            main_result = main_func(*args, **kwargs)
            if main_result is not None:
                return main_result

            after_result = after_func(*args, **kwargs)
            if after_result is not None:
                return after_result

        return wrapper
    return outer 

@time_calcuate
@func_filter(func_before, func_after)
def index(*args, **kwargs):
    print(args)
    print(kwargs)

index('a','b', a=1, b=2)








