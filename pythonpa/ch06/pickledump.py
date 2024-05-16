import pickle                               #导入模块
with open(r'c:\pythonpa\dataObj1.dat', 'wb') as f:  #打开文件（二进制写入模式）
    s1='Hello!'                            #写入字符串
    c1=1+2j                              #写入复数
    t1=(1,2,3)                            #写入元组
    d1=dict(name='Mary', age=19)           #写入字典
    pickle.dump(s1, f)                     #将字符串对象保存到文件中
    pickle.dump(c1, f)                    #将复数对象保存到文件中
    pickle.dump(t1, f)                    #将元组对象保存到文件中
    pickle.dump(d1, f)                    #将字典对象保存到文件中
