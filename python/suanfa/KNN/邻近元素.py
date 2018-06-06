
from 欧式距离函数 import euclidean_distance
import operator

from datetime import datetime as dt 
# 装饰器-测试函数运行时间
def time_calcuate(func):
    def inner(*args, **kwargs):
        start = dt.now()
        ret = func(*args, **kwargs)
        delta = dt.now() - start 
        print('elapsed time:' , delta.microseconds)
        return ret   
    return inner 


@time_calcuate
def get_neighbors(trainingSet, testInst, k):
    distances = []
    length = len(testInst)-1

    for x in range(len(trainingSet)):
        dist = euclidean_distance(testInst, trainingSet[x], length)
        distances.append((trainingSet[x], dist))

    
    distances.sort(key=operator.itemgetter(1)) # 根据第二个元素进行排序
    print('all neighbors:%s'  %distances)
    
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])

    return neighbors

trainSet = [[2,2,2,'a'], [4,4,4,'b'], [3,2,3,'c'], [4,5,7,'d']]
testInstance = [5,5,5]
k = 2 
neighbors = get_neighbors(trainSet, testInstance, k)
print(neighbors)

