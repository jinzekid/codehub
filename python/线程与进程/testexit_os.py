# Author: Jason Lu
"""
对于try/except和try/finally截获对os._exit均不起作用
"""
def outahere():
    import os
    print('Bye os world')
    os._exit(99)
    print('Never reached')

if __name__ == '__main__': outahere()