import matplotlib.pyplot as plt	#导入模块
import numpy as np			#导入模块
x = np.linspace(0,10,100)		#生成x坐标点的列表
y = x*x					#y = x*x
plt.plot(x, y)				#绘制图形
plt.show()					#显示图形
