import math                         	#导入模块
m = int(input("请输入一个整数(>1)："))  	#提示输入整数，并将字符串转换为整数
k = int(math.sqrt(m))                  	#取整数m的平方根 
flag = True                   			#先假设所输入的整数为素数
i = 2                        			#while循环赋初值
while (i <= k and flag == True):  			#判断循环条件
    if (m % i == 0):           			#整除运算余数为0，表示可以整除 
        flag = False          			#可以整除，肯定不是素数，结束循环
    else:
        i += 1              			#循环计数值加1，继续循环
if (flag == True):             			#素数判断标志一直为True
    print(m, "是素数！")     			#m是素数
else:                       			#素数判断标志被修改为False
    print(m, "是合数！")     			#m是合数

