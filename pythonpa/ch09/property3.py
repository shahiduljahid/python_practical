class Person13:              #定义类Person13
    def __init__(self, name):  #__init__方法（构造函数）
        self.__name = name  #初始化self.name，即成员变量name
    def getname(self):       #定义类方法getname()
        return self.__name   #返回成员变量name
    def setname(self, value):   #定义类方法setname()
        self.__name = value  #设置成员变量name的值
    def delname(self):        #定义类方法delname()
        del self.__name      #删除成员变量name
    name = property(getname, setname, delname, "I'm the 'name' property.")
#测试代码
p = Person13('爱丽丝');print(p.name)
p.name = '罗伯特'; print(p.name)
