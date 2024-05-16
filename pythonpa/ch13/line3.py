import matplotlib.pyplot as plt     #导入模块
import numpy as np             #导入模块
x = np.linspace(0,10,10)         #生成x值的列表
plt.plot(x, x * 0.5)              #绘制图形y = 0.5x
plt.plot(x, x * 5)                #绘制图形y = 5x
plt.plot(x, x * x)                #绘制图形y = x^2
#plt.plot(x, x*0.5, x, x*5, x, x*x)   #也可以使用一条语句同时绘制多个图形
plt.show()                     #显示图形
