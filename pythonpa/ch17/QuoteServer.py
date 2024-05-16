import socket, random 					#导入socket和random模块
quotes = ['不妄求，则心安，不妄做，则身安','三人行，必有我师','随遇而安',
          '人之心胸，多欲则窄，寡欲则宽', '滴水穿石，磨杵成针','命为志存',
         '是非天天有，不听自然无','积德为产业，强胜于美宅良田']
#创建服务器socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind(('127.0.0.1', 8002)) 		#绑定到IP地址和端口号
while 1: 						#循环以接收和回送客户机数据
    data, address = serversocket.recvfrom(1024) 	#接收数据，返回数据和客户机地址
    quote = random.choice(quotes) 			#从Quotes列表中随机选择一个项目
    serversocket.sendto(quote.encode(), address) 	#数据转换为bytes对象后发送数据到客户机
serversocket.close()             			#关闭服务器socket
