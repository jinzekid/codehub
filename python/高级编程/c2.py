#!/Users/jasonlu/.virtualenvs/pyven3_6/bin/python 
# 列表推导式
ret = [i for i in range(10) if i % 2 ==0]
print(ret)

def _treatment(pos, element):
    return '%d: %s' %(pos, element)

seq = ['one', 'two', 'three']
ret= [_treatment(i, el) for i, el in enumerate(seq)]
print(ret)
