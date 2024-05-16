import numpy as np                   #导入numpy模块
import matplotlib.pyplot as plt           #导入matplotlib模块中的子模块pyplot
#随机生成满足mu为100、sigma为20的正态分布的10万个智商数据
mu, sigma = 100, 20
x = mu + sigma * np.random.randn(100000)
plt.hist(x, bins=50)  #绘制直方图
plt.xlabel('IQ')                               #绘制x轴坐标标题
plt.ylabel('Probability')                        #绘制y轴坐标标题
plt.title('Histogram of IQ')                     #绘制图表标题
plt.grid(True)                               #显示网格
plt.show()                                  #绘制直方图
