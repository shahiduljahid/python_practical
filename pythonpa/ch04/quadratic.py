import math, sys            	#导入模块
b = float(sys.argv[1])    		#获取命令行参数argv[1]，并转换为浮点数b
c = float(sys.argv[2])    		#获取命令行参数argv[2]，并转换为浮点数c
discriminant = b*b - 4.0*c  		#计算方程判别式的值
if discriminant>=0:        		#判别式大于等于0
    d = math.sqrt(discriminant)	#判别式开平方根
    print("x1=",(-b + d) / 2.0)		#计算并输出方程的实数解1
    print("x2=",(-b - d) / 2.0)		#计算并输出方程的实数解2
else:
    print("此方程无实数解")  
