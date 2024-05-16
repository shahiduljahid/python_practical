import sys   #导入sys模块
import turtle                     #导入turtle模块
def koch(t, order, size):
        if order == 0:            #当n等于0时，绘制一条直线
            t.forward(size)
        else:                    #否则，递归绘制n阶科赫曲线
            koch(t, order-1, size/3)  #递归绘制一条阶数为n-1的科赫曲线，长度1/3
            t.left(60.0)            #向左旋转60度
            koch(t, order-1, size/3)  #递归绘制一条阶数为n-1的科赫曲线，长度1/3
            t.right(120.0)  #t.left(-120.0) #向右旋转120度（或者向左旋转-120度）
            koch(t, order-1, size/3)   #递归绘制一条阶数为n-1的科赫曲线，长度1/3
            t.left(60.0)             #向左旋转60度
            koch(t, order-1, size/3)   #递归绘制一条阶数为n-1的科赫曲线，长度1/3
def main():
        n = int(sys.argv[1])   #n阶科赫曲线
        step = 300          #步长
        p = turtle.Turtle()    #创建海龟对象
        koch(p, n, step)     #绘制n阶科赫曲线
if __name__ == '__main__': main()  #如果独立运行时，则运行测试代码
