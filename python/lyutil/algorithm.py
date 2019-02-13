'''
快速排序方法
'''
def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

def quick_sort(seq):
    if len(seq) <= 1: return seq
    lo, pi, hi = partition(seq)
    return quick_sort(lo) + pi + quick_sort(hi)




