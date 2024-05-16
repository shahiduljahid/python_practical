class Fib:                            #定义类
    def __init__(self):                 #构造函数
        self.a,self.b = 0,1              #前两项值分别为0和1
    def __next__(self):                 #定义__next__()方法
        self.a, self.b = self.b, self.a+self.b  #第三项是前两项之和
        return self.a                   #f(n)=f(n-1)+f(n-2)
    def __iter__(self):                  #定义__iter__()方法
        return self                    #返回可迭代对象（迭代器）
#测试代码
fibs = Fib()                           #创建实例对象
for f in fibs:                          #对于可迭代对象（迭代器）中每一个元素
    if f < 1000: print(f, end=',')          #元素值<1000则输出（逗号分隔）
    else: break                       #元素值≥1000则跳出for循环
