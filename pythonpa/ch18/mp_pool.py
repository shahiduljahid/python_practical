from multiprocessing import Pool, TimeoutError
import time
import os
def f(x):
    return x*x  #返回x的平方
if __name__ == '__main__':
    # 创建四个进程的进程池，并调用其对象方法并行执行各任务
    with Pool(processes=4) as pool:
        # 使用进程池对象map函数，并行计算并返回结果
        res1 = pool.map(f, range(10))
        print("pool.map的结果：{}".format(res1))
        # 使用进程池对象的apply_async函数，异步执行一次任务
        res2 = pool.apply_async(f, (20,))      # 异步求解f(20)，仅使用一个进程
        print(res2.get(timeout=1))             # 输出结果：400
        res3 = pool.apply_async(os.getpid, ()) #异步执行os.getpid()，仅使用一个进程
        print(res3.get(timeout=1))             #输出执行任务的进程的PID
        res4 = pool.apply_async(time.sleep, (10,)) #异步睡眠10秒钟
        try:
            print(res4.get(timeout=1))    #尝试获得结果，等待超时为1秒钟
        except TimeoutError:
            print("结果超时！")
        #使用列表解析式，可能使用多个进程
        res5 = [pool.apply_async(os.getpid, ()) for i in range(5)]
        print([res.get(timeout=1) for res in res5])
        print("在With语句中，进程池可用")
    print("在With语句之外，进程池自动关闭，不再可用")
