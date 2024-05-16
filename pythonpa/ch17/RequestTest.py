import urllib.request   					#导入urllib.request模块
def getURLInfo(url, data, headers):			#定义函数，获取URL信息
    req = urllib.request.Request(url, data, headers) 	#创建Request对象
    print('Full url:', req.full_url)  			#URL
    print('Host:', req.host)       			#主机和端口号
    print('Data:', req.data)       			#向服务器传送的数据
if __name__=='__main__':    				#如果独立运行时，则运行测试代码
    url = 'http://www.baidu.com/'  
    values = {'wd':'python'}  
    data = urllib.parse.urlencode(values)			#URL编码
    data = data.encode(encoding='UTF8')		#编码为utf-8
    headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    getURLInfo(url, data, headers)			#调用函数
