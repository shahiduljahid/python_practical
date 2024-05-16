import time
import multiprocessing as mp
def productor(i, q):
    while True:
        time.sleep(1)  #休眠1秒钟，即每秒钟做一个包子
        q.put("厨师{}做的包子！".format(i)) #如果队列满，则等待
def consumer(j, q):
    while True:
        print("顾客{}吃了一个{}" .format(j, q.get())) #如果队列空，则等待
        time.sleep(1) #休眠1秒钟，即每秒钟吃一个包子
if __name__=='__main__':
    q = mp.Queue(10) #创建一个大小为10的队列
    for i in range(3): #3个厨师不停做包子，
        p = mp.Process(target=productor, args=(i,q))
        p.start()
    for k in range(10): #10个顾客等待吃包子
        p = mp.Process(target=consumer, args=(k,q))
        p.start()
