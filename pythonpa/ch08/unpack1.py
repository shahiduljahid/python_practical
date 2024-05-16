#参数解包：在函数调用中使用1个星（*）将序列解包为多个参数
def sum1(a, b, c):         #对参数进行累加和
    return a + b + c
list = [1, 2, 4]            #一个列表
res = sum1(*list)         #等价于res = sum1(1, 2, 4)
print("参数解包：", res)
