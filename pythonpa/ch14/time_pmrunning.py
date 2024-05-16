import time                    #导入模块
def test():                      #返回1+2+…+9999998的累加和
    total = 0                   #累加和初值为0
    for i in range(1,9999999):     #i=1~9999998
        total += i               #i累加到total中
    return total                  #返回累计和
if __name__=='__main__':       #如果独立运行时，则运行测试代码
    t1 = time.monotonic()       #单向时钟
    print(test())               #调用并输出累加和
    t2 = time.monotonic()       #单向时钟
    print('运行时间：', t2-t1)    #本程序所花费的运行时间
