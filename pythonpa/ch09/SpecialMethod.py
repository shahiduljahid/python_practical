class Person:                         #定义类
    def __init__(self, name, age):        #特殊方法（构造函数）
        self.name = name             #参数name赋值给self.name，即成员变量name
        self.age = age                #参数age赋值给self.name，即成员变量age
    def __str__(self):                  #特殊方法，输出成员变量
        return '{0}, {1}'.format(self.name,self.age) #输出姓名和年龄
#测试代码
p1 = Person('张三', 23)                        #创建实例对象
print(p1)                                   #输出对象
