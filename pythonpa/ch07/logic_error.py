import math                      #导入模块
a=1; b=2; c=1                    #为一元二次方程各个系数赋值
x1 = -b + math.sqrt(b*b-4*a*c)/2*a  #公式有误，故结果不正确
x2 = -b - math.sqrt(b*b-4*a*c)/2*a  #公式有误，故结果不正确
print(x1, x2)                    #输出：-2.0 -2.0
