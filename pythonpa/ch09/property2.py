class Person12:              #定义类Person12
    def __init__(self, name):   #__init__方法（构造函数）
        self.__name = name  #初始化self.name，即成员变量name
    @property             #装饰器
    def name(self):
        return self.__name  #返回成员变量name
    @name.setter          # setter装饰器
    def name(self, value):
        self.__name = value #设置成员变量name的值
    @name.deleter        #deleter装饰器
    def name(self):
        del self.__name   #删除成员变量name
#测试代码
p = Person12('姚六')
p.name = '王依依'
print(p.name)
