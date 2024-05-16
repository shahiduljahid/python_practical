import matplotlib.pyplot as plt	#导入模块
import numpy as np			#导入模块
x = np.linspace(0, 10, 100)		#生成x轴的列表数据（范围[0,10]中的100个点）
fig1 = plt.figure()				#创建一个Figure对象
ax1 = fig1.add_subplot(2,1,1)		#创建一个子图：2行1列中的第1个图
ax1.plot(x, np.sin(x))			#绘制y = sin(x)
ax1.set_title('sin(x)')			#设置图表标题
ax2 = fig1.add_subplot(2,1,2)		#创建一个子图：2行1列中的第2个图
ax2.plot(x, np.cos(x))				#绘制y = cos(x)
ax2.set_title('cos(x)')			#设置图表标题
plt.show()					#显示图形
