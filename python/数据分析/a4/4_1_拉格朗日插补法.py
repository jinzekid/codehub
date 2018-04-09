# Author: Jason Lu
import pandas as pd
import xlwt
from scipy.interpolate import lagrange #导入拉格朗日插值函数

inputfile = 'data/catering_sale.xls'
outputfile = 'tmp/sales.xls'

#读入数据
data = pd.read_excel(inputfile)
# print(data.describe())
# print(data.shape)
# print(data.info())
# print(data.columns)


# 过滤异常值, 将其变为空值
data.loc[(data['销量'] > 5000) | (data['销量'] < 400), '销量'] = None

# print(data)
# data_filter_none = data['销量'].fillna(value=0)
# print(data_filter_none)

# data_filter.loc[data_filter['销量']] = None
# filter_expection_data = data_filter
# print(filter_expection_data)



# print(data.head(n=len(data)))
# print(data.tail())
#
# print(data['销量'] < 400)
# print(data['销量'] > 5000)
#
# #过滤异常值，将其变为空值
# data['销量'][(data['销量'] < 400 | data['销量'] > 5000)] = None
#
#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为去前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s[list(range(n-k,n)) + list(range(n+1, n+1+k))] #取数
    y = y[y.notnull()] #剔除空值
    return lagrange(y.index, list(y))(n) #插值并返回插值结果

# 逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            r = ployinterp_column(data[i], j)
            print(i, j, r)
            data[i][j] = ployinterp_column(data[i], j)
            # print(data[i][j])

data.to_excel(outputfile) #输出结果，写入文件
print("end....")


