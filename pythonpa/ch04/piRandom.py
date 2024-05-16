import random
def piRandom(trials):
    """通过随机点位置近似计算圆周率pi"""
    hits = 0   #命中圆环的点的数量
    for i in range(trials):
        x = random.uniform(-1,1) #随机生成-1到1之间的x坐标
        y = random.uniform(-1,1) #随机生成-1到1之间的y坐标
        if x**2+y**2 <= 1: #如果位于圆环内，则命中数加1
            hits += 1
    return 4*hits/trials
#测试代码
if __name__ == "__main__":
    for i in range(5):
        n = 10000*(10**i)
        print("试验{}次后计算近似圆周率为：{}".format(n, piRandom(n)))
