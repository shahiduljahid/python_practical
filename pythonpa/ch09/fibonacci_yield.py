def fib():                          #定义生成器函数
    a,b = 0,1                       #前两项值
    while True:                     #一直循环
        a,b = b,a+b                 #第三项是前两项之和
        yield a               #f(n)=f(n-1)+f(n-2)
if __name__ == '__main__':  #如果独立运行时，则运行测试代码
    fibs = fib()                   #调用生成器函数，返回可迭代对象
    for f in fibs:                  #对于可迭代对象（迭代器）中每一个元素
        if f < 1000:           #如果元素值<1000
            print(f, end=',')  #输出（逗号分隔）
        else:                  #如果元素值≥1000
            break              #跳出for循环
