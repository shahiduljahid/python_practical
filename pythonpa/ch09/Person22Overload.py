class Person22:              #定义类Person22
    def say_hi(self, name):    #定义类方法say_hi()，带两个参数
        print('您好, 我叫', self.name)
    def say_hi(self, name, age): #定义类方法say_hi()，带三个参数
        print('hi, {0}, 年龄：{1}'.format(name,age))
p22 = Person22()          #创建实例对象
p22.say_hi('Lisa', 22)       #调用对象的方法
p22.say_hi('Bob')         #TypeError: say_hi() missing 1 required 
# positional argument: 'age'
