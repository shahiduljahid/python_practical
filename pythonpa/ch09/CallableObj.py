class GDistance:                     #定义类：自由落体距离
    def __init__(self, g):               #构造函数
        self.g = g                     #重力加速度参数g赋值给self.g，即成员变量g
    def __call__(self, t):                 #计算并返回自由落体下落距离
        return (self.g*t**2)/2
if __name__ == '__main__':               #如果独立运行时，则运行测试代码
    e_gdist = GDistance(9.8)              #地球上的重力加速度
    for t in range(11):                     #自由落体0~10秒的下落距离
        print(format(e_gdist(t), "0.2f"),end=' ') #调用可调用对象e_gdist
