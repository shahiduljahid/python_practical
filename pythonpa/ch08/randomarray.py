import random     #导入模块
def randomarray(n): #生成由n个随机数构成的列表
    a = []
    for i in range(n):  #0~n-1循环迭代
        a.append(random.random()) #将[0,1)之间的随机数添加到列表中
    return a                     #返回由n个随机数构成的列表
#测试代码
b=randomarray(5)     #生成由5个随机数构成的列表
for i in b: print(i) #输出列表中每个元素
