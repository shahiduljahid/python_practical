import sys               #导入模块
total = 0.0               #设置数值汇总初值
count = 0                #设置数值计数初值
for line in sys.stdin:       #对标准输入流中的数值循环迭代
    count += 1          #计数加1
    total +=float(line)     #数值汇总累加
avg = total / count         #计算数值平均值
print("平均值为：",avg)   #输出数值平均值
