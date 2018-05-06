#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python
"""
计算球体的直径，圆周长，表面积和体积
"""
import math
#import numpy as np
def func():
    b_isLoop = True 
    while b_isLoop:        
        str_raduis = (input("请输入球体半径(q或Q退出):"))
        
        if str_raduis in ['q', 'Q']:
            print('Bye...')
            break
        if str_raduis == '':
            continue

        flt_raduis = float(str_raduis)
        flt_zc = 2 * math.pi * flt_raduis
        print("球体的圆周长:%.2f" %(flt_zc))
        flt_bmj = 4 * math.pi * math.pow(flt_raduis, 2)
        print("球体表面积:%.2f" %(flt_bmj))
        flt_tj = float(4 * math.pi * math.pow(flt_raduis, 3) / 3)
        print("球体体积:%.2f" %(flt_tj))
        print('-----------------------------')

func()

