import matplotlib.pyplot as plt           #导入matplotlib模块中的子模块pyplot
import math                          #导入math模块
x = [2*math.pi*i/100 for i in range(100)]   #x轴的取值范围
y = [math.sin(i) for i in x]               #y=sin(x)
plt.plot(x, y)
plt.show()                          #绘制函数曲线
