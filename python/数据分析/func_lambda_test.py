from math import log

def make_logarithmic_function(base):
    return lambda x: log(x, base)

My_LF = make_logarithmic_function(3)

print(My_LF(9))


