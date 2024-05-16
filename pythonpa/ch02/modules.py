import math                         #导入标准模块math
a = 1; b = -5; c = 6                    #变量a、b和c分别指向int对象1、-5和6
x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)  #使用模块math中的函数sqrt求解平方根
x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
print('方程x*x + 5*x + 6 = 0的解为：', x1, x2)  #输出一元二次方程的两个解
