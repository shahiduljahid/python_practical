import matplotlib.pyplot as plt   #导入模块
import numpy as np            #导入模块
x = np.linspace(0,8,100)       #生成x坐标点的列表
plt.axis([0,8,10,80])         #设置两个坐标轴的范围
plt.plot(x, 10 + x*x)           #绘制图形
plt.show()                   #显示图形
