import smtplib				#导入模块
def prompt(prompt):				#定义应答函数
    return input(prompt).strip()
fromaddr = prompt("From: ")		#发件人地址
toaddrs  = prompt("To: ").split()		#收件人地址
print("输入信息，^D (Unix) or ^Z (Windows)结束输入：")
# 添加From:和To:头信息
msg = ("From: %s\r\nTo: %s\r\n\r\n"% (fromaddr, ", ".join(toaddrs)))
while True:					#一直循环
    try:
        line = input()			#提示用户输入信息
    except EOFError:			#EOF异常处理
        break
    if not line:				#用户未输入信息
        break				#跳出循环
    msg = msg + line			#拼接用户输入信息
print("信息长度为：", len(msg))				#信息长度
server = smtplib.SMTP('localhost')			#SMTP对象
server.set_debuglevel(1)					#设置调试级别
server.sendmail(fromaddr, toaddrs, msg)			#发送邮件
server.quit()							#注销退出
