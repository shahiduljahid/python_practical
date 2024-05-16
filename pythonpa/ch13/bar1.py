import matplotlib.pyplot as plt              #导入模块
plt.rcParams['font.sans-serif']=['SimHei']      #用来正常显示中文标签
#确定柱状图数量,可以认为是x轴刻度（地区：华中、华南、华东、华北、华西）
x=[1,2,3,4,5]
y=[5,7,4,3,1]                             #y轴刻度（销售额，单位：百万）
color=['red','black','green','orchid','blue']  #颜色列表（红、黑、绿、淡紫色、蓝）
x_label=['华中','华南','华东','华北','华西']      #x轴刻度标签
plt.xticks(x, x_label)                       #绘制x轴刻度标签
plt.bar(x, y,color=color)                    #绘制y轴刻度标签
plt.xlabel('地区')                         #绘制x轴坐标标题
plt.ylabel('销售额（单位：百万）')         #绘制y轴坐标标题
plt.title('各地区产品年度销售额')           #绘制图表标题
plt.grid(True,linestyle=':',color='r',alpha=0.6)  #设置网格刻度
plt.show()                              #绘制柱状图
