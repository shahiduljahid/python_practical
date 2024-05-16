import matplotlib.pyplot as plt		#导入模块
import numpy as np				#导入模块
x = np.linspace(0,10,100)			#生成x坐标点的列表
plt.plot(x, np.sin(x), x, np.cos(x)) 		#绘制正弦曲线和余弦曲线
plt.axis(xmin=0, xmax=11, ymin=-1.1, ymax=1.1)	#设置两个坐标轴范围
plt.xlabel('x') 							#设置x轴的标签
plt.ylabel('y') 							#设置y轴的标签
plt.legend(['sin(x)','cos(x)'],loc='upper right') 		#设置图例
plt.savefig('plot1.png') 					#保存图形到文件
plt.show()  							#显示图形
