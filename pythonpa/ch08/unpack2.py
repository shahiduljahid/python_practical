def display(a, b, c):             #显示参数值的函数
    print(a, b, c)
kwargs = {"a": 1, "b": 2, "c": 3}  #字典数据
display(**kwargs)             #等价于display(a=1,b=2,c=3)
display(a=1, b=2, c=3)          #调用函数
