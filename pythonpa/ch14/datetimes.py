import datetime                    #导入模块
d = datetime.date.today()             #当前日期
dt = datetime.datetime.now()          #当前时间
print ("当前的日期是 %s" % d)
print ("当前的日期和时间是 %s" % dt)
print ("ISO格式的日期和时间是 %s" % dt.isoformat() )
print ("当前的年份是 %s" %dt.year)
print ("当前的月份是 %s" %dt.month)
print ("当前的日期是  %s" %dt.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (dt.day, dt.month, dt.year) )
print ("当前小时是 %s" %dt.hour)
print ("当前分钟是 %s" %dt.minute)
print ("当前秒是  %s" %dt.second)
