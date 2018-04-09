# Author: Jason Lu
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='$\sin x+1$', color='red', linewidth=2)
plt.plot(x, z, 'b--', label='$\cos x^2+1$')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('A Simple Example(一个示例)')
plt.ylim(0, 2.2)
plt.legend()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()