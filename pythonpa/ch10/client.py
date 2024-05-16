import math, sys                	#导入模块
n = int(sys.argv[1])             	#命令行第一个参数的值，转换为整数
for i in range(n+1):              	#i=0~n
    x = math.pi * i / n           	#x坐标值（[0,pi]区间）
    y = math.sin(x) + math.sin(5 * x)	#y坐标值
    print(x, y)
