import socket 									#导入socket模块
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	#创建客户机socket
#循环以接收用户输入，并发送到服务器，接收服务器的回送数据
while 1:
    data = input('>')                   					#接收用户输入数据
    #把数据转换为bytes对象，并发送到服务器
    clientsocket.sendto(data.encode(),('127.0.0.1', 8000))
    if not data:									#接收到空数据
        break 									#终止循环
    newdata = clientsocket.recvfrom(1024) 					#接收服务器的回送数据
    print('Received from server: ', repr(newdata)) 				#输出接收到数据
clientsocket.close()                    					#关闭客户机socket
