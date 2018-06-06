# Author: Jason Lu
import numpy as np
a = np.arange(5)
print(a.dtype) # 在pylab中输出，dtype('int64')

#创建一个多维数组
import numpy as np
m = np.array([np.arange(2),np.arange(2)])
m
m.shape

print("---------------------------------------")
# 创建自定义数据类型
t = np.dtype([('name',      np.dtype('U40')),
              ('numitems',  np.dtype('int32')),
              ('price',     np.dtype('float32'))
              ])
print(t)

itemz = np.array([('Meaning of life DVD', 42, 3.14),
                  ('Butter', 13, 2.72)], dtype=t)
print(itemz[0])

# 文件读写示例
i2 = np.eye(2)
print(i2)
np.savetxt('eye.txt', i2)





