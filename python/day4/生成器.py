# Author: Jason Lu

b = ( i * 2 for i in range(10) )
print(b, type(b))
# output: <generator object <genexpr> at 0x105250f68> <class 'generator'>

print(b.__next__())
print(b.__next__())

print("\n======================\n")
# 访问的时候才生成
for i in b:
    print(i)


print("\n==========生成器============\n")
# 通过函数做了一个生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b # 相当于中断后可以再次回来
        a, b = b, a + b

        # 相当于
        '''
        t = (b, a + b) # t是一个tuple
        a = t[0]
        b = t[1]
        '''
        n = n + 1

    # return "done"

fib_gen = fib(5)
print("==================")
# 通过next，超出长度，就会抛出异常
while True:
    try:
        x = next(fib_gen)
        print("g:", x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break

