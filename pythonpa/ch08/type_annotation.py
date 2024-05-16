def area(r: float) -> float:  #使用形参：类型注解形参类型，使用->类型注解返回值类型
    res: float = 3.14 * r * r #使用变量名：类型注解变量类型
    return res
r1 = 1.2                #圆的半径为1.2
print(area(r1))           #调用函数，计算并输出圆的面积
