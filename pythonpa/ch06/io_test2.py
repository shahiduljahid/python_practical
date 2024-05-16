import datetime
sName = input("请输入您的姓名：")           #输入姓名
birthyear = int(input("请输入您的出生年份："))  #输入出生年份
age = datetime.date.today().year - birthyear    #根据当前年份和出生年份计算年龄
print("您好！{0}。您{1}岁。".format(sName, age))
