import threading, time, random
def timer(interval):
    for i in range(3):
        time.sleep(random.choice(range(interval))) #随机睡眠interval秒
        thread_id = threading.get_ident()          #获取当前线程标识符
        print('Thread:{0} Time:{1}'.format(thread_id, time.ctime()))
if __name__=='__main__':
    t1 = threading.Thread(target=timer, args=(5,)) #创建线程
    t2 = threading.Thread(target=timer, args=(5,)) #创建线程
    t1.start(); t2.start()                       #启动线程
