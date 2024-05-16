import concurrent.futures as cf
import math, time
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    # 测试数据
    test_data = [112272535095293, 112272535095293, 115280095190773, 1099726899285419]
    # 串行处理测试
    start_time = time.time()  # 结束时间
    for num in test_data:
        print('{}是素数否：{}'.format(num, is_prime(num)))
    end_time = time.time()
    print("串行处理消耗时间：{}".format(end_time - start_time))
    # 并行处理测试
    start_time = time.time()  # 开始时间
    with cf.ProcessPoolExecutor() as executor:
        primes = executor.map(is_prime, test_data)
        for number, prime in zip(test_data, primes):
            print('{}是素数否：{}'.format(number, prime))
    end_time = time.time()
    print("并行处理消耗时间：{}".format(end_time - start_time))
