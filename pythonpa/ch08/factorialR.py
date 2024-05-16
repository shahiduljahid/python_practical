def myFactorial(n):
    if n == 1: return 1         #中止条件
    return n * myFactorial(n - 1)   #递归步骤
#测试代码
for i in range(1,10):          #输出1~9的阶乘
    print(i,'! =', myFactorial(i))
