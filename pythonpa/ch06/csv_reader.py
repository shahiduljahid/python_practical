import csv                           	#导入模块
def readcsv1(csvfilepath):               	#定义使用reader对象读取CSV文件的函数
    with open(csvfilepath, newline='') as f:	#打开文件（使用默认的只读文本文件格式）
        f_csv = csv.reader(f)    		#创建csv.reader对象
        headers = next(f_csv)   		#标题
        print(headers)         		#打印标题（列表）
        for row in f_csv:      			#循环打印各行（列表）
            print(row)
if __name__ == '__main__':     			#独立运行时则运行测试代码
    readcsv1(r'scores.csv')     			#函数调用
