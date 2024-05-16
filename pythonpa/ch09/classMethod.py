class Foo:
    classname = "Foo"
    def __init__(self, name):   #__init__方法（构造函数）
        self.name = name     #初始化self.name，即成员变量name
    def f1(self):              #实例方法
        print(self.name)      #输出成员变量name的值
    @staticmethod  
    def f2():                #静态方法  
        print("static")  
    @classmethod  
    def f3(cls):             #类方法
        print(cls.classname)  
#测试代码
f = Foo("李")                #创建实例对象
f.f1()                       #调用对象的实例方法
Foo.f2()                    #调用静态方法
Foo.f3()                    #调用类方法
