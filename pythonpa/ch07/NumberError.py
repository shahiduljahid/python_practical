class NumberError(Exception):  			#自定义异常类，继承于Exception
    def __init__(self,data):    			#构造函数
        super().__init__(data) 			#调用基类构造函数
        self.data = data      			#数据成员
    def __str__(self):        			#重载__str__()方法
        return self.data + ': 				非法数值(< 0)' 
def total(data):              			#数值数据累加和
    total = 0               			#累加和初值为0
    for i in data:            			#循环迭代每个数据
        if i < 0: raise NumberError(str(i))	#负数则抛出异常
        total += i          			#否则，累加非负数数值数据
    return total            			#返回非负数数据的累加和
#测试代码
data1 = (44, 78, 90, 80, 55)   			#创建元组数据
print('总计=', total(data1))   				#元组数据汇总
data2 = (44, 78, 90, -80, 55)  				#创建元组数据
print('总计=', total(data2))   				#元组数据汇总
