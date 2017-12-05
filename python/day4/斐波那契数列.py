# Author: Jason Lu

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b

        # 相当于
        '''
        t = (b, a + b) # t是一个tuple
        a = t[0]
        b = t[1]
        '''

        n = n + 1

    return "done"

fib(10)

