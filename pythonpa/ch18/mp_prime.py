import math
import time
import multiprocessing

def isprime(n):
    """判断n是否为素数，如果是，返回n，否则返回0"""
    if n < 2:
        return 0
    if n == 2:
        return n
    k = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= k:
        if n % i == 0:
            return 0
        i += 1
    return n

if __name__ == "__main__":
    #测试数据
    test_data = range(10**6)
    # 串行处理测试
    start_time = time.time()  # 结束时间
    with open("prime1.txt", "w") as outf:
        for num in test_data:
            r = isprime(num)
            if r > 0:
                outf.writelines("{}\n".format(num))
    end_time = time.time()
    print("串行处理消耗时间：{}".format(end_time - start_time))
    # 并行处理测试
    start_time = time.time()  # 开始时间
    pool = multiprocessing.Pool(4)
    resultList = pool.map(isprime, test_data)
    pool.close()
    pool.join()
    with open("prime2.txt", "w") as outf:
        for r in resultList:
            if r > 0:
                outf.writelines("{}\n".format(r))
    end_time = time.time()  # 结束时间
    print("并行处理消耗时间：{}".format(end_time - start_time))
