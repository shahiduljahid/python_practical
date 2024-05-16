import pickle                           	#导入模块
with open(r'c:\pythonpa\dataObj1.dat', 'rb') as f:	#打开文件（二进制读取模式）
    o1=pickle.load(f)                    	#从文件中读取并重构1个对象
    o2=pickle.load(f)                    	#从文件中读取并重构1个对象
    o3=pickle.load(f)                    	#从文件中读取并重构1个对象
    o4=pickle.load(f)                    	#从文件中读取并重构1个对象
    print(type(o1), str(o1))               		#输出对象的数据类型以及内容
    print(type(o2), str(o2))               		#输出对象的数据类型以及内容
    print(type(o3), str(o3))               		#输出对象的数据类型以及内容
    print(type(o4), str(o4))               		#输出对象的数据类型以及内容
