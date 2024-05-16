import sys              #导入模块
def harmonic(n):         #计算n阶调和数（1 + 1/2 + 1/3 + … + 1/n）
    total = 0.0           #累加和total初值为0
    for i in range(1, n+1):  #从1到n进行循环迭代
        total += 1.0 / i    #累加和
    return total          #返回n阶调和数的值
n = int(sys.argv[1])       #从命令行第一个参数中获取调和数阶数
for i in range(1, n+1):     #输出前n个调和数的值
    print(harmonic(i))    #调用函数
