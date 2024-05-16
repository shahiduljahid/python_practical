class Person11:            #定义类Person11
    def __init__(self, name): #__init__方法（构造函数）
        self.__name = name #初始化self.name，即成员变量name
    @property            #装饰器
    def name(self):
        return self.__name #返回成员变量name
#测试代码
p = Person11('王五')
print(p.name)
