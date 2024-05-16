class Point:                        #定义类
    def __init__(self, x = 0, y = 0):    #__init__方法（构造函数）
        self.x = x                 #成员变量x赋值
        self.y = y                 #成员变量y赋值
p1 = Point()                       #创建实例对象
print("p1({0},{1})".format(p1.x, p1.y))  #访问并输出成员变量的值
p2 = Point(5, 5)                    #创建实例对象
print("p2({0},{1})".format(p2.x, p2.y))  #访问并输出成员变量的值
