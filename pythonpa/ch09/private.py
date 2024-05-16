class A:              		#定义类A
    __name = 'class A' 		#私有类属性
    def get_name():   		#定义类A的方法get_name()
        print(A.__name)	#在类方法中访问私有类属性
#测试代码
A.get_name()       		#调用类方法
A.__name          		#错误！不能直接访问私有类属性
