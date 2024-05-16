import matplotlib.pyplot as plt    #导入模块
import numpy as np            #导入模块
x = np.random.randn(1000)      #生成由1000个随机点组成的x坐标
y = np.random.randn(1000)      #生成由1000个随机点组成的y坐标
size = np.random.randn(1000)    #生成由1000个随机点组成的大小
colors = np.random.rand(1000)   #生成由1000个随机点组成的颜色
plt.scatter(x, y, s=size, c=colors)  #绘制由1000个随机点组成的散点图
plt.show()                    #显示图形
