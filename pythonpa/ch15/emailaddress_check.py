import os, re						#导入模块
def check_email(strEmail):				#定义函数
    #正则表达式对象
    regex_email = re.compile(r'^[\w\.\-]+@([\w\-]+\.)+[\w\-]+$') 
    result = True if regex_email.match(strEmail) else False 
    return result
if __name__=='__main__':				#如果独立运行时，则运行测试代码
    str1 = "hjiang@yahoo.com"			#有效的电子邮箱
    str2 = "hjiang.yahoo.com"			#无效的电子邮箱
    print(str1,'是有效的电子邮件格式吗？', check_email(str1))
    print(str2,'是有效的电子邮件格式吗？', check_email(str2))
