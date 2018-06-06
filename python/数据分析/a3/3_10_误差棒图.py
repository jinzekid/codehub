# Author: Jason Lu
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt #导入图像库
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.figure(figsize=(7, 5)) #创建图像区域，指定比例

import numpy as np
import pandas as pd

error = np.random.randn(10) #定义误差列
y = pd.Series(np.sin(np.arange(10))) #均值数据列
y.plot(yerr=error)
plt.show()