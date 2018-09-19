# Author: Jason Lu
import os
import time
import sys
mypid = os.getpid()
parentid = os.getppid()
sys.stderr.write('Child %d of %d got arg: "%s"\n' %(mypid, parentid,
                                                    sys.argv[1]))

for i in range(3):
    time.sleep(3)
    recv = input()
    time.sleep(3)
    send = 'Child %d got: [%s]' % (mypid, recv)
    print(send)
    sys.stdout.flush() # 确保数据已经发送，否则阻塞进程

