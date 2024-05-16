import sqlite3				#导入模块
#打开SQLite数据库：c:\Pythonpa\ch16\sales.db
con = sqlite3.connect(r"c:\Pythonpa\ch16\sales.db")
#查询数据库表的记录内容
cur = con.execute("select id, name from region")
for row in cur:   #循环输出结果
    print(row)
con.close()
