# 堆排序
def swap(L, a, b):
    tmp = L[a]
    L[a]= L[b]
    L[b] = tmp
    
# 向下调整结点
def sift_down(L, n, i):
    t = i;
    flag = 0
    
    # 左右结点的判断
    while i <= n/2 and flag == 0:
        if L[i] > L[i*2]:
            t = i*2
        else:
            t = i
            
        if 2*i+1 <= n:
            if L[t] > L[i*2+1]:
                t = i*2+1
                
        if i != t:
            swap(L, i, t)
            i = t;
        else:
            flag = 1

            
# 向上调整结点
def sift_up(L, i):
    k = i
    flag = 0
    
    if i == 1:
        return
    
    # 叶子结点和根结点的判断
    while k > 1 and flag == 0:
        if L[k] > L[k/2]:
            swap(L, k, k/2)
            k = k/2
        else:
            flag = 1


def create_heap(L, n):
    i = int(n/2)
    while i >=1:
        sift_down(L, n, i)
        i -= 1
    
def heap_sort(L, n):
    k = n
    while k > 0:
        swap(L, 1, k)
        k -= 1
        sift_down(L, k, 1)

if __name__ == "__main__":
    k = 0
    # 读取n个数
    n = int(input())
    # 输入列表
    input_L = list(map(int, input().split()))
    L = [""] + input_L
    
    # 创建堆序列
    create_heap(L, n)
    
    print("排序前:")
    print(L)
    print("\n")
    heap_sort(L, n)
    print("排序后:")
    print(L)
    print("\n")
