a = int(input("请输入第1个整数："))		#输入整数1
b = int(input("请输入第2个整数："))		#输入整数2
print(str.format("输入值：{0}, {1}", a, b)) 	#显示所输入的两个整数
if (a < b):        					#如果a小于b
    a, b = b, a					#a和b交换
print(str.format("降序值：{0}, {1}", a, b)) 	#输出降序排序结果
