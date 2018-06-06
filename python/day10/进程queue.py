# Author: Jason Lu
# 父进程的q和子进程的q不是同一个q
# 相当于克隆了一份，但是又通过pickle反序列化给父进程的q（有点疑惑）

from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])


# 手动执行就会执行
if __name__ == '__main__':
    q = Queue() # 父进程的q
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())  # prints "[42, None, 'hello']"
    p.join()

