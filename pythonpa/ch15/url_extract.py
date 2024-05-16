import re, urllib.request					#导入模块
def url_extract(homepage):					#定义函数
    regex_href = re.compile(r'href="(.+?)"')		#正则表达式对象
    f = urllib.request.urlopen(homepage)			#打开网页
    webcontents = f.read().decode()			#网页内容解码
    matches = regex_href.finditer(webcontents)		#查找超链接地址
    for m in matches:
        print(m.group(1))					#输出匹配的组
if __name__=='__main__': 				#如果独立运行时，则运行测试代码
    www = r'http://www.baidu.com'			#指定网页
    url_extract(www)					#从中查找所有超链接地址
