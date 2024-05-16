import matplotlib.pyplot as plt         #导入模块
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
labels = ['住房','餐饮','娱乐','其他']
explode = (0, 0.1, 0, 0.1)  #分离出第2个&第4个切片（'餐饮'和'其他'）
percentages = [60.2, 20.5, 15.1, 4.2]                 #饼图百分比
plt.pie(percentages,explode=explode,labels=labels,autopct='%1.1f%%', shadow=True) 
plt.title("9月份家庭支出占比")
plt.show()
