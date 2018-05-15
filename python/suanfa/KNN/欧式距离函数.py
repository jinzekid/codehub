#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python 
import math
"""
欧式距离函数
用于KNN算法，计算两列数中对应数做差的平方和，之后再开方
多维数组距离计算，length为数组长度
"""
def euclidean_distance(inst1, inst2, length):
    distance = 0
    for x in range(length):
        distance += pow((inst1[x] - inst2[x]), 2)

    return math.sqrt(distance)


"""
# 测试代码
data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']

distance = euclidean_distance(data1, data2, 3)
print('Distance:' + str(distance))
"""
