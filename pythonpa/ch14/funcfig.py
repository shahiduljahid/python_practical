import numpy as np					#导入模块
import matplotlib.pyplot as plt 			#导入模块
import math						#导入模块
x = np.linspace(0, 10, 100)			#x轴坐标值
y1 = np.power(x,2)					#y1=x**2
y2 = np.exp2(x)					#y2=2**x
plt.plot(x, y1, x, y2)					#绘制图形
plt.show()						#显示图形
