import functools                       #导入模块
@functools.total_ordering               #装饰器
class Student:                         #定义类
    def __init__(self, firstname, lastname):  #构造函数
        self.firstname = firstname         #名
        self.lastname = lastname          #姓
    def __eq__(self, other):               #判断姓名是否一致
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):               #self姓名<other姓名
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
if __name__ == '__main__':             #如果独立运行时，则运行测试代码
    s1 = Student('Mary','Clinton')               #创建实例对象1
    s2 = Student('Mary','Clinton')               #创建实例对象2
    s3 = Student('Charlie','Clinton')             #创建实例对象3
    print(s1==s2)                           #s1是否等于s2？
    print(s1>s3)                            #s1是否大于s2？
