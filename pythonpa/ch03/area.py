import math                            #导入模块
a = float(input("请输入三角形的边长a：")) #提示输入边长a，并转换为浮点数
b = float(input("请输入三角形的边长b：")) #提示输入边长b，并转换为浮点数
c = float(input("请输入三角形的边长c：")) #提示输入边长c，并转换为浮点数
h = (a + b + c) / 2                       #三角形周长的一半
area = math.sqrt(h*(h-a)*(h-b)*(h-c));       #三角形面积
print(str.format("三角形三边分别为：a={0},b={1},c={2}", a, b, c)) #输出三角形的三边
print(str.format("三角形的面积 = {0}", area)) #输出三角形的面积
