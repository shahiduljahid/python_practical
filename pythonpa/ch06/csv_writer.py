import csv                            		#导入模块
def writecsv1(csvfilepath):    				#定义使用writer对象写入CSV文件的函数
    headers = ['学号', '姓名', '性别', '班级', '语文', '数学', '英语']
    rows = [('102111', '宋颐园', '男', '一班', '72', '85', '82'),
            ('102113', '王二丫', '女', '一班', '75', '82', '51')]
    with open(csvfilepath,'w', newline='') as f:	#打开文件（写入模式）
        f_csv = csv.writer(f)               	#创建csv.writer对象
        f_csv.writerow(headers)            	#写入1行（标题）
        f_csv.writerows(rows)              	#写入多行（数据）
if __name__ == '__main__':                 	#独立运行时则运行测试代码
    writecsv1(r'scores1.csv')                	#函数调用
