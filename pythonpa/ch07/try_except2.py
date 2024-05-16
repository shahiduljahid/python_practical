a = (44, 78, 90, -80, 55)                      #创建一个元组
total = 0                                  #累计和初值为0
try:
    for i in a:                             #循环迭代元组中的每一个元素
        if i < 0: raise ValueError(str(i)+"为负数") #元素值小于0，抛出异常
        total += i                          #元素值大于等于0，累加
    print('合计=', total)                      #输出元素累加和
except Exception:
    print('发生异常')
except ValueError:
    print('数值不能为负')
