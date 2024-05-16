import time
import queue
import threading
q = queue.Queue(10) #创建一个大小为10的队列
def productor(i):
    while True:
        time.sleep(1)  #休眠1秒钟，即每秒钟做一个包子
        q.put("厨师{}做的包子！".format(i)) #如果队列满，则等待
def consumer(j):
    while True:
        print("顾客{}吃了一个{}" .format(j, q.get())) #如果队列空，则等待
        time.sleep(1) #休眠1秒钟，即每秒钟吃一个包子
for i in range(3): #3个厨师不停做包子，
    t = threading.Thread(target=productor, args=(i,))
    t.start()
for k in range(10): #10个顾客等待吃包子
    v = threading.Thread(target=consumer, args=(k,))
v.start()
