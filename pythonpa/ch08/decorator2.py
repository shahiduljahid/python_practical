def makebold(fn):					#定义函数
    def wrapper(*s):
        return "<b>" + fn(*s) + "</b>"		#利用标签实现加粗
    return wrapper
def makeitalic(fn): 					#定义函数
    def wrapper(*s):
        return "<i>" + fn(*s) + "</i>"		#利用标签实现斜体
    return wrapper
@makebold                        	#装饰器（用于加粗）
@makeitalic                       	#装饰器（用于斜体）
def htmltags(str1):                  	#定义HTML标签函数
    return str1
#测试代码
print(htmltags('Hello'))              		#添加加粗斜体的HTML标签
