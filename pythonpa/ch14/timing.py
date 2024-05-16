import time,random            #导入模块
def piRandom(trials):           #定义函数
    """通过随机点位置近似计算圆周率pi"""
    hits = 0                   #命中圆环的点的数量
    for i in range(trials):         #i=0~trials-1
        x = random.uniform(-1,1) #随机生成-1到1之间的x坐标
        y = random.uniform(-1,1) #随机生成-1到1之间的y坐标
        if x**2+y**2 <= 1:     #如果位于圆环内，则命中数加1
            hits += 1
    return 4*hits/trials          #返回圆周率的值
def timing(f, data):
    """测量函数调用f(data)的运行时间分析"""
    start = time.time()       #记录开始时间
    f(data)                #运行f(data)
    end = time.time()        #记录结束时间
    return end - start         #返回执行时间
if __name__ == "__main__":   #如果独立运行时，则运行测试代码
    for i in range(3):         #i=0~2
        n = 10000*(100**i)
        t = timing(piRandom, n)
        print("pi({})的运行时间为：{}".format(n, t))
