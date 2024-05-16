import multiprocessing as mp
import time, random, itertools
def consumer(conn):
    #从管道读取数据
    while True:
        try:
            item = conn.recv()
            time.sleep(random.randrange(2))  #随机休眠,代表处理过程
            print("consume:{}".format(item))
        except EOFError:
            break
def producer(conn):
    #生产项目并将其发送到连接的管道上
    for i in itertools.count(1): #从1开始无限循环
        time.sleep(random.randrange(2)) #随机休眠,代表处理过程
        conn.send(i)
        print("produce:{}".format(i))
if __name__=="__main__":
    # 创建管道，返回2个连接对象的元组
    conn_out, conn_in = mp.Pipe()
    # 创建并启动生产者进程，传入参数管道一端的连接对象
    p_producer = mp.Process(target=producer, args=(conn_out,))
    p_producer.start()
    # 创建并启动消费者进程，传入参数管道另一端的连接对象
    p_consumer = mp.Process(target=consumer, args=(conn_in,))
    p_consumer.start()
    #加入进程，等待完成
    p_producer.join(); p_consumer.join()
import multiprocessing as mp
import time, random, itertools
def consumer(conn):
    #从管道读取数据
    while True:
        try:
            item = conn.recv()
            time.sleep(random.randrange(2))  #随机休眠,代表处理过程
            print("consume:{}".format(item))
        except EOFError:
            break
def producer(conn):
    #生产项目并将其发送到连接的管道上
    for i in itertools.count(1): #从1开始无限循环
        time.sleep(random.randrange(2)) #随机休眠,代表处理过程
        conn.send(i)
        print("produce:{}".format(i))
if __name__=="__main__":
    # 创建管道，返回2个连接对象的元组
    conn_out, conn_in = mp.Pipe()
    # 创建并启动生产者进程，传入参数管道一端的连接对象
    p_producer = mp.Process(target=producer, args=(conn_out,))
    p_producer.start()
    # 创建并启动消费者进程，传入参数管道另一端的连接对象
    p_consumer = mp.Process(target=consumer, args=(conn_in,))
    p_consumer.start()
    #加入进程，等待完成
    p_producer.join(); p_consumer.join()
