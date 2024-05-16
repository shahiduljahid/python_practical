import matplotlib.pyplot as plt                    #导入模块
plt.rcParams['font.sans-serif']=['SimHei']            #用来正常显示中文标签
labels = ['住房','餐饮','娱乐','其他']                 #饼图标签
percentages = [60.2, 20.5, 15.1, 4.2]                 #饼图百分比
plt.pie(percentages,labels=labels,autopct='%1.1f%%')  #饼图参数
plt.title("9月份家庭支出占比")                   #绘制图标标题
plt.show()                                     #绘制饼图
