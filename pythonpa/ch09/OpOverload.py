class MyList:                       #定义类MyList
    def __init__(self, *args):          #构造函数
        self.__mylist = []            #初始化私有属性，空列表
        for arg in args:               #对args中的元素迭代
            self.__mylist.append(arg)  #添加元素到列表中
    def __add__(self, n):              #重载运算符"+"，每个元素增加n
        for i in range(0, len(self.__mylist)): #对列表中的元素迭代
            self.__mylist[i] += n        #列表中的每个元素增加n
    def __sub__(self, n):                #重载运算符"-"，每个元素减少n
        for i in range(0, len(self.__mylist)): #对列表中的元素迭代
            self.__mylist[i] -= n         #列表中的每个元素减少n
    def __mul__(self, n):                #重载运算符"*"，每个元素乘以n
        for i in range(0, len(self.__mylist)): #对列表中的元素迭代
            self.__mylist[i] *= n        #列表中的每个元素乘以n
    def __truediv__(self, n):             #重载运算符"/"，每个元素除以n
        for i in range(0, len(self.__mylist)): #对列表中的元素迭代
            self.__mylist[i] /= n         #列表中的每个元素除以n
    def __len__(self):                  #对应于内置函数len()，返回列表长度
        return(len(self.__mylist))
    def __repr__(self):                 #对应于内置函数str()，显示列表
        str1 = ''
        for i in range(0, len(self.__mylist)):
            str1 += str(self.__mylist[i]) + ' '
        return str1
#测试代码
m = MyList(1, 2, 3, 4, 5)               #创建对象
m + 2; print(repr(m))                 #每个元素加2
m - 1; print(repr(m))                 #每个元素减1
m * 4; print(repr(m))                 #每个元素乘以4
m / 2; print(repr(m))                 #每个元素除以2
print(len(m))                       #列表长度
