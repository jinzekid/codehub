# 快速排序
def swap(L, a, b):
    tmp = L[a]
    L[a]= L[b]
    L[b] = tmp

def quick_sort(L, low, high):
    
    if low >= high:
        return
    
    tmp = L[low];
    left = low
    right = high
    
    while left < right:
        while right > left and L[right] >= tmp:
            right -= 1
        while left < right and L[left] <= tmp:
            left += 1
        
        if left != right:
            swap(L, left, right)
         
    if low != left:
        swap(L, left, low)
            
    quick_sort(L, low, left-1)
    quick_sort(L, left+1, high)
    

if __name__ == "__main__":
    # 读取n个数
    n = int(input())
    # 输入列表
    L = list(map(int, input().split()))
    
    print("排序前:")
    print(L)
    print("\n")
    quick_sort(L, 0, n-1)
    print("排序后:")
    print(L)
    print("\n")
