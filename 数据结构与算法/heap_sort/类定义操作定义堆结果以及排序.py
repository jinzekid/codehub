# 类结构的堆排序
class DLinkHeap(object):
    def __init__(self, list=None, N = 0):
        self.dList = list
        self.lengthSize = N
        
    # 插入数据
    def insert_heap(self, data):
        self.dList.append(data)
        self.lengthSize += 1    
        
    # 初始化堆结构
    def init_heap(self):
        n = self.lengthSize
        for i in range(n):
            self.sift_down(i)
    
    # 交换数据
    def swap(self, a, b):
        tmp = self.dList[a]
        self.dList[a] = self.dList[b]
        self.dList[b] = tmp
    
    # 向下调整节点
    def sift_down(self, size):
        n = size
        t = 0
        tmp_pos = 0
        
        # 注意python的/运算，是取浮点数
        while t < int(n/2):
            if self.dList[t] > self.dList[2*t+1]:
                tmp_pos = 2*t+1
            else:
                tmp_pos = t
        
            if 2*t+2 < n:
                if self.dList[tmp_pos] > self.dList[2*t+2]:
                    tmp_pos = 2*t+2
        
            if t != tmp_pos: 
                self.swap(tmp_pos, t)
                t = tmp_pos
            else:
                break
    
    # 向上调整节点
    def sift_up(self, size):
        n = size
        i = n - 1
        flag = 0
        
        while i > 0 and flag == 0:
            parent_i = int(i/2)
            if self.dList[i] < self.dList[parent_i]:
                self.swap(i, parent_i)
                i = parent_i
            else:
                flag = 1

    # 堆排序 
    def heap_sort(self):
        n = self.lengthSize
        while n > 0:
            self.swap(0, n-1)
            n -= 1
            self.sift_down(n)

    # 打印堆数据
    def print_heap(self, size):
        for idx in range(size):
            print(self.dList[idx], end=" ")
        print()

       
if __name__ == "__main__":
    k = 0
    # 读取n个数
    n = int(input())
    # 输入列表
    input_L = list(map(int, input().split()))
    L = input_L
    dLinkHeap = DLinkHeap(L, n)
    dLinkHeap.init_heap()
    dLinkHeap.print_heap(n)
    print("-----after sort-----")
    dLinkHeap.heap_sort()
    dLinkHeap.print_heap(n)
        
        
