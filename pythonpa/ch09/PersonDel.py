class Person3:                #定义类
    count = 0                #定义类域count，表示计数
    def __init__(self, name,age): #__init__方法（构造函数）
        self.name = name     #参数name赋值给self.name，即成员变量name（域）
        self.age = age        #参数age赋值给self.age，即成员变量age（域）
        Person3.count += 1   #每创建一个实例时，计数加1
    def __del__(self):        #析构函数
        Person3.count -= 1   #每销毁一个实例时，计数减1
    def say_hi(self):        #定义类Person3的方法say_hi()
        print('您好, 我叫', self.name)
    def get_count():        #定义类Person3的方法get_count()
        print('总计数为：', Person3.count)
print('总计数为：',Person3.count)        #类名访问
p31 = Person3('张三',25)               #创建实例对象
p31.say_hi()                         #调用对象的方法
Person3.get_count()                   #通过类名访问
p32 = Person3('李四',28)               #创建实例对象
p32.say_hi()                         #调用对象的方法
Person3.get_count()                   #通过类名访问
del p31                             #删除对象p31
Person3.get_count()                   #通过类名访问
del p32                             #删除对象p32
Person3.get_count()                  #通过类名访问
