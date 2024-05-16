import random                    #导入模块
def gamble2(stake, goal, trials):
    """返回筹码stake赢得goal的概率，模拟仿真trials次取平均值"""
    bets = 0      #总下注次数
    wins = 0      #赢的次数
    for t in range(trials):#模拟trials次取平均
        cash = stake  #筹码
        #持续下注直到破产，或达到目标退场
        while cash > 0 and cash < goal:  #循环条件
            #模拟一次下注
            bets += 1                    #总下注次数加1
            if random.randrange(0, 2) == 0:  #随机生成0
                cash += 1                #筹码加1
            else:                       #随机生成1
                cash -= 1               #筹码减1 
        if cash >= goal:
            wins += 1                   #赢的次数 
    return wins/trials, int(bets/trials)        
if __name__ == "__main__":   #如果独立运行时，则运行测试代码
    p, n = gamble2(10,20,100)
    print("{}赢{}的概率{}%，平均下注次数{}".format(10,20,p*100,n))
    p, n = gamble2(10,1000,100)    #调用函数
    print("{}赢{}的概率{}%，平均下注次数{}".format(10,1000,p*100,n))
