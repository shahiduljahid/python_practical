from collections import *               #导入模块
import csv                           #导入模块
EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv"))):
    print(emp.name, emp.title)          #输出职工姓名和职称
