class CustomAttribute(object):        #定义类
    def __init__(self):              #__init__方法（构造函数）
        pass                     #空语句
    def __getattribute__(self, name):  #获取属性
        return str.upper(object.__getattribute__(self, name))
    def __setattr__(self, name, value): #设置属性
        object.__setattr__(self, name, str.strip(value))
#测试代码
o = CustomAttribute()              #创建实例对象
o.firstname='      mary     '      #设置成员变量的值
print(o.firstname)                 #读取并显示成员变量的值
