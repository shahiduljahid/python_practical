nb = float(input("请输入本金："))    		#输入本金并转换为浮点数
nr = float(input("请输入年利率："))  		#输入年利率并转换为浮点数
ny = int(input("请输入年份："))    		#输入年份并转换为整数
amount = nb * (1+nr/100) ** ny			#计算复利
print("本金利率和为：%0.2f"%amount)	#输出复利，保留两位小数
