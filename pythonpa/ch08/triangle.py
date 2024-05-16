import sys               #导入模块
def print_star(n):          #定义打印星号的函数
    print(("*"*n).center(50)) #打印n个星号，两边填充空格，总宽度50
lines = int(sys.argv[1])      #三角形行数
for i in range(1, 2*lines,2):   #每行打印1、3、5、...、2*lines-1个星号
    print_star(i)           #调用打印星号的函数
