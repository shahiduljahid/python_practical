import sqlite3				#导入模块
#创建SQLite数据库：c:\Pythonpa\ch16\sales.db
con = sqlite3.connect(r"c:\Pythonpa\ch16\sales.db")
#创建表regions，包含两个列，id（主码）和name
con.execute("create table region(id primary key, name)")
