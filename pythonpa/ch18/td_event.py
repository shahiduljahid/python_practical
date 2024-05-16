import threading
import random
def f(i, e):
    e.wait()   #检测Event的标志，如果是False则阻塞
    print("线程{}的随机结果为{}".format(i, random.randrange(1,100)))
if __name__ == '__main__':
    event = threading.Event() #创建事件对象，默认标志为False
    for i in range(3): #创建3个线程并运行，默认阻塞等待Event
        t = threading.Thread(target=f, args=(i, event))
        t.start()
    ready = input('请输入1开始继续执行阻塞的线程：')
    if ready == "1":
        event.set()  #设置Event的flag为True
