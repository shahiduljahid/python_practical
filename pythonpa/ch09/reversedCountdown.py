class Countdown:             #定义类
    def __init__(self, start):    #构造函数
        self.start = start       #参数start赋值给self.start，即成员变量start
    #正向迭代
    def __iter__(self):         #定义__iter__()方法，从大到小迭代
        n = self.start
        while n > 0:
            yield n
            n -= 1
    #反向迭代
    def __reversed__(self):       #定义__reversed__()方法，从小到大迭代
        n = 1
        while n <= self.start:
            yield n
            n += 1
if __name__ == '__main__':          #如果独立运行时，则运行测试代码
    for i in Countdown(10):          #正向迭代
        print(i, end=' ')             #输出10~1，空格分隔
    for i in reversed(Countdown(10)):  #反向迭代
        print(i, end=' ')             #输出1~10，空格分隔
