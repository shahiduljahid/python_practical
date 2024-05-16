import time, random
import multiprocessing as mp
def timer(interval):
    for i in range(3):
        time.sleep(random.choice(range(interval))) #随机睡眠interval秒
        pid = mp.current_process().pid     #获取当前进程ID
        print('Process:{0} Time:{1}'.format(pid, time.ctime()))
if __name__=='__main__':
    p1 = mp.Process(target=timer, args=(5,))  #创建进程
    p2 = mp.Process(target=timer, args=(5,))  #创建进程
    p1.start(); p2.start()                    #启动线程
    p1.join(); p2.join()
