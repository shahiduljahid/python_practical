import sys           #导入模块
n = int(sys.argv[1])   #命令行第一个参数确认所需求和的整数个数n
total = 0            #设置求和初始值=0
for i in range(n):
    number = int(input('请输入整数：')) #输入整数
    total += number                 #整数累加
print('累计和为：', total)    #输出n个整数累计和
