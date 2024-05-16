import re						#导入模块
def html_txt(htmlwithtag):				#定义函数
    regex_href = re.compile(r'<.+?>')		#正则表达式对象
    return regex_href.sub('', htmlwithtag)	#替换为空''，并返回替换结果
if __name__=='__main__':				#如果独立运行时，则运行测试代码
    htmltext = r'<a href=\"index.html\">Welcome to Python world!</a>'
    print(html_txt(htmltext))			#输入字符串中清除了HTML标记
