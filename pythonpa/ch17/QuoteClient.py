import socket 						#导入socket模块
#创建客户机socket 
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
clientsocket.sendto(b'hello',('127.0.0.1', 8002)) 		#数据转换为bytes对象后发送到服务器
newdata, address = clientsocket.recvfrom(1024) 	#接收服务器的回送数据
print('今日名言: ', newdata.decode()) 			#接收到数据解码为字符串，并输出
clientsocket.close()               			#关闭客户机socket
