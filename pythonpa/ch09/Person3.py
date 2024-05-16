class Person3:         		#定义类Person3
    count = 0         		#定义属性count，表示计数
    name = "Person"   		#定义属性name，表示名称
#测试代码
Person3.count += 1       	#通过类名访问，将计数加1
print(Person3.count)      	#类名访问，读取并显示类属性
print(Person3.name)       	#类名访问，读取并显示类属性
p1 = Person3()            	#创建实例对象1
p2 = Person3()            	#创建实例对象2
print((p1.name, p2.name))	#通过实例对象访问，读取成员变量的值
Person3.name = "雇员"     	#通过类名访问，设置类属性值
print((p1.name, p2.name))   	#读取成员变量的值
p1.name = "员工"          	#通过实例对象访问，设置实例对象成员变量的值
print((p1.name, p2.name))   	#读取成员变量的值
