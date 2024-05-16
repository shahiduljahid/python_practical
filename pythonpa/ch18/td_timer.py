import threading
def f():
    print('Hello Timer!')
    global timer
    timer = threading.Timer(1, f) #创建定时器，1秒后运行
    timer.start()

timer = threading.Timer(1, f) #创建定时器，1秒后运行
timer.start() #启动定时器