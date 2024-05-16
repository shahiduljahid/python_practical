def vertical(n):               #定义递归函数
    """依次垂直输出整数各个位数上的数字"""
    if n < 10:                #终止条件：n为1位数时，直接输出
        print(n)
    else:                    #递归步骤：当为多位数时，整除10后递归调用
        vertical(n//10)
        print(n%10)          #输出余数
if __name__ == "__main__":    #如果独立运行时，则运行测试代码
    vertical(123687)
