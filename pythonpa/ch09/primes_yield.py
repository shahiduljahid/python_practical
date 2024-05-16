import math                          #导入模块
def is_prime(n):                       #定义生成器函数
    if n < 2: return False                #<2则返回False
    if n == 2: return True               #=2则返回True（2是素数）
    if n % 2 == 0: return False           #能被2整除则返回False
    sqrt_n = int(math.floor(math.sqrt(n)))  #n的平方根
    for i in range(3, sqrt_n + 1, 2):        #从3到n的平方根进行循环，步长2
        if n % i == 0:                  #如果n整除i，则返回False
            return False
    return True
def primes(m, n):
    """返回[m, n]之间所有素数的生成器函数"""
    for i in range(m, n+1):              #从m到n循环迭代
        if is_prime(i):                 #如果i是素数，则返回i
            yield i
if __name__ == '__main__':             #如果独立运行时，则运行测试代码
    pimes1 = primes(5000000000, 5000000090)  #调用生成器函数，返回可迭代对象
    for p in pimes1:                        #对于可迭代对象（迭代器）中每一个元素
        print(p, end=',')                    #输出素数（逗号分隔）
