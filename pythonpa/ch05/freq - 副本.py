import turtle            #导入海龟模块
def freq_table(data_list):  #统计列表data_list中的值的个数，返回包含值计数的字典
    countDict = {}      #创建储存频数的字典k：值，v：计数
    for item in data_list:  #统计列表data_list中的值的个数
        countDict[item] = countDict.get(item,0) + 1
    return countDict
def draw_freq(freq_dict):   #绘制值计数的字典freq_dict的直方图
    itemList = list(freq_dict.keys())    #获取键的列表
    maxItem = len(itemList) - 1       #获取最大项目数
    itemList.sort()                 #对键的列表排序
    countList = freq_dict.values()    #获取计数的列表
    maxCount = max(countList)     #获取最大的计数值
    #使用海龟对象，绘制直方图
    wn = turtle.Screen()            #创建海龟绘图窗口
    t = turtle.Turtle()              #创建海龟对象
    wn.setworldcoordinates(-1, -1, maxItem + 1, maxCount + 1) #设置绘图窗口大小
    t.hideturtle()                  #隐藏海龟
    t.up();t.goto(0, 0);t.down()      #绘制基准线(X轴)  
    t.goto(maxItem, 0); t.up()
    for i in range(0,maxCount+1):   #绘制Y轴标签
        t.goto(-1, i)
        t.write(str(i), font=("Helvetica", 16, "bold"))
    for index in range(len(itemList)):
        t.goto(index, -1)           #绘制标签
        t.write(str(itemList[index]),font=("Helvetica",16,"bold"))
        t.goto(index, 0)            #绘制计数线条（高度）
        t.down()
        t.goto(index, freq_dict[itemList[index]])
        t.up()
    wn.exitonclick()              #单击鼠标关闭绘图窗口
data = [3,1,2,1,3,1,2,2,3,5,3,5,4,5,3,4,5,2,3,3,2,2,3,4,2,5,4,3]
freq_dict = freq_table(data)         #返回频数字典
#打印结果
itemList = list(freq_dict.keys())     #获取键的列表
itemList.sort()                   #对键的列表排序
print("值", "计数")
for item in itemList:              #打印频数值及计数
    print(item, " ", freq_dict[item]) 
draw_freq(freq_dict)             #绘制频数表所对应的直方图
