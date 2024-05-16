import math                        #导入模块
a = 3.0                            #边长a
b = 4.0                            #边长b
c = 5.0                            #边长c
h = (a + b + c) / 2                   #三角形周长的一半
s = math.sqrt(h*(h-a)*(h-b)*(h-c))     #三角形面积
print(s)                           #输出三角形面积
