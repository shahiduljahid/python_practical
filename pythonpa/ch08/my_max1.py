def my_max1(a, b):          #定义求最大值的函数
    if a > b: print(a, '>', b)    #a大于b
    elif a == b: print(a, '=', b)  #a等于b
    else: print(a, '<', b)       #a小于b
my_max1(1, 2)              #调用函数
x = 11; y = 8
my_max1(x, y)              #调用函数
my_max1(1)                #调用函数（参数个数不对）
