# IPython log file

get_ipython().run_line_magic('clear', '')
get_ipython().run_line_magic('logstart', '')
#创建一个多维数组
import numpy as np
m = np.array([np.arange(2),np.arange(2)])
m
m.shape
get_ipython().run_line_magic('hist', '')
m3 = np.array([np.arange(3),np.arange(3),np.arange(3)])
m3
m3.shape
a = np.array([1,2],[3,4])
a = np.array([[1,2],[3,4]])
a
a[0,0]
a[0,1]
a[1,1]
a[1,0]
float64(42)
int8
int8(42.0)
np.int8(42.0(
)
)
np.int8(42.0)
np.bool(0)
np.arange(7, dtype=uint16)
np.arange(7, dtype=np.uint16)
a.dtype.itemsize
np.arange(7, dtype='D')
np.arange(7, dtype='f')
np.arange(7, dtype='2f')
np.arange(7, dtype='.2f')
np.arange(7, dtype='3f')
np.arange(7, dtype='4f')
np.arange(7, dtype='f')
np.dtype(float)
np.dtype('f')
np.dtype('d')
np.dtype('f8')
np.sctypeDict.keys()
np.dtype('int64')
np.dtype('p')
np.dtype('Float64')
t = dtype('Float64')
t = np.dtype('Float64')
t.char
t.type
t.str
t = np.dtype('str_')
t
t = np.dtype('string')
t = np.dtype('str')
t = np.dtype('str40')
t = np.dtype('str')
a = np.arange(9)
a[3:7]
a[:7:2]
a[::-1]
b = np.arange(24)
b.reshape(2,3,4)
b.shape
b = b.reshape(2,3,4)
b.shape
b
b = np.arange(24).reshape(2,3,4)
b
b[0,0,0]
b[:0,0]
b[:,0,0]
b[0]
b[0::]
b[0,:,:]
b[0,...]
b[0,1]
b[0,0,1]
b[0,1,:]
b[0,1,::2]
b[,:,:,1]
b[,:,:1]
b[:,:,1]
b[:,1,:]
b[0,:,1]
b[0,:,-1]
b[0,:,-2]
b[0,:,-1, -1]
b[0,::-1, -1]
b[0,::2, -1]
b[::-1]
b[::-1, -1]
b[::1, -1]
b
b.ravel()
b.flatten()
b.shape = (6,4)
b
b.transpose()
b.resize(2,12)
b
a = np.arange(9).reshape(3,3)
a
b = 2 * a
b
hstack
hstack((a, b))
np.hstack((a, b))
help(np.concatenate)
