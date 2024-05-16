import socket                     						#导入socket模块
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	#创建客户机socket
clientsocket.connect(('127.0.0.1', 8001)) 						#连接到服务器
#循环以接收用户输入，并发送到服务器，接收服务器的回送数据
while 1:
    data = input('>')             						#接收用户输入数据
    clientsocket.send(data.encode()) 						#数据转换为bytes对象并发送到服务器
    if not data: break             						#如果数据为空，终止循环
    newdata = clientsocket.recv(1024) 						#接收服务器的回送数据
    print('Received from server: ', repr(newdata)) 				#输出接收到数据
clientsocket.close()                						#关闭客户机socket
