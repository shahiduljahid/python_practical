import csv    					#导入模块
scores = []    					#创建列表存储从csv文件中读取的成绩信息
csvfilepath = 'data.csv'            		#指定数据文件（原始成绩信息）
with open(csvfilepath, newline='') as f:	#打开文件（文本读取模式）
    f_csv = csv.reader(f)     			#创建csv.reader对象
    headers = next(f_csv)    			#标题信息
    for row in f_csv:        			#循环打印各行内容
        scores.append(row)
print("原始记录:",scores)
scoresData = []     				#创建列表存储成绩的统计信息
for rec in scores:    				#循环遍历成绩记录列表（学号姓名成绩）
    scoresData.append(int(rec[2]))  	#形成学生成绩的列表
print("成绩列表:",scoresData)      	#输出学生成绩列表
print("平均成绩:",sum(scoresData)/len(scoresData))	#输出平均成绩
