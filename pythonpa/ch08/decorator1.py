import time, functools               #导入模块
def timeit(func):                   #装饰器
    def wrapper(*s):
        start = time.perf_counter()   #性能计数
        func(*s)                 #调用函数
        end = time.perf_counter()   #性能计数
        print('运行时间:', end - start) #程序运行时间
    return wrapper
@timeit
def my_sum(n):              #计算0~n-1的累加和
    total = 0
    for i in range(n): total += i  #从0累加到n-1
    print(total)
if __name__ == '__main__':  #如果独立运行时，则运行测试代码
    my_sum(100000)
