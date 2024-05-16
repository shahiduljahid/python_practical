num = 0; scores = 0;              #初始化学生人数和成绩和
while True:                     #循环条件
    s = input('请输入学生成绩（按Q或q结束）：') #提示输入成绩
    if s.upper() == 'Q':                           #输入了Q或q
        break                        #跳出循环，结束循环的执行
    if float(s) < 0:                     #成绩必须>=0
        continue                     #跳转到循环开始，继续判断循环条件
    num += 1                        #统计学生人数
    scores += float(s)                  #汇总成绩
print('学生人数为：{0}，平均成绩为：{1}'.format(num,scores / num)) #输出学生人数和平均成绩
