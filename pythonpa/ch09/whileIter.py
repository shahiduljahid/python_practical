t=(1,2,3,4,5,6,7,8,9,0)           #元组
fetch=iter(t)                   #获取迭代器
while True:                    #一直循环
    try:
        i=next(fetch)          #获得下一个项目
    except StopIteration:        #如果没有新项目
        break                #跳出while循环
    print(i, end=' ')            #依次输出项目值，空格分隔

