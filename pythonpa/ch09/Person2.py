class Person2:                 	#定义类Person2
    def __init__(self, name,age): 	#__init__()方法（构造函数）
        self.name = name     		#初始化self.name，即成员变量name（域）
        self.age = age        		#初始化self.age，即成员变量age（域）
    def say_hi(self):         		#定义类Person2的方法say_hi()
        print('您好, 我叫', self.name)	#在实例方法中通过self.name读取成员变量
#测试代码
p1 = Person2('张三',25)       		#创建实例对象
p1. say_hi ()               		#调用实例对象的方法
print(p1.age)              		#通过p1.age（obj1.变量名）读取成员变量
