a=[]                						#初始化列表
x=float(input("请输入一个实数，输入-1终止："))	#提示用户输入实数
while x != -1:
    a.append(x)    							#将所输入的实数添加到列表中
    x=float(input("请输入一个实数，输入-1终止："))
print("计数：", len(a))     					#列表长度即为实数个数
print(f"求和：{sum(a):0.2f}")  						#列表中各元素累加和
avgs=sum(a)/len(a)
print(f"平均值：{avgs:0.2f}")					#列表中各元素求平均值
