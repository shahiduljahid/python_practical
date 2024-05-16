class Book:                          #定义类Book
    def __init__(self, name, author, price): #__init__方法（构造函数）
        self.name = name            #参数name赋值给self.name，即成员变量name（域）
        self.author = author          #参数author赋值给self.author，即成员变量author（域）
        self.price = price            #参数price赋值给self.price，即成员变量price（域）
    def __check_name(self):          #定义私有方法，判断name是否为空
        if self.name == '' :
            return False
        else:
            return True
    def get_name(self):              #定义类Book的方法get_name()
        if self.__check_name():
            print(self.name,self.author) #调用私有方法
        else:
            print('No value')
b = Book('Python程序设计教程','江红 余青松',59.0)    #创建实例对象
b.get_name()                              #调用对象的方法
#b.__check_name()                          #直接调用私有方法，非法
