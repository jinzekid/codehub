# Author: Jason Lu
"""
在python中设置和捕获定时暂停信号，time.sleep和定时（或者在linux pc上的一般信号操作）
合用效果不好，所以，在这里调用signal.pause来暂停操作，知道接受到信号
"""
import sys, signal, time
def now(): return time.asctime()

def onSignal(signum, stackframe):
    print('Got alarm', signum, 'at', now())


while True:
    print('Setting at', now())
    signal.signal(signal.SIGALRM, onSignal) # 布置信号处理器
    signal.alarm(5)                         # 5秒后发送信号
    signal.pause()                          # 等待信号

