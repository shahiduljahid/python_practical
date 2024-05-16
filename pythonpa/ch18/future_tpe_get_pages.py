import concurrent.futures as cf
import time, urllib.request
def load_page(url):
    with urllib.request.urlopen(url, timeout=60) as conn:
        return ('{}主页大小：{}字节'.format(url, len(conn.read())))
if __name__ == '__main__':
    URLS = ['http://www.163.com', 'http://www.sina.com.cn/', 'http://www.sohu.com/']
    # 传统串行方法
    start_time = time.time()
    for url in URLS:
        print(load_page(url))
    end_time = time.time()
    print("串行处理消耗时间：{}".format(end_time - start_time))
    # 使用ThreadPoolExecutor并发处理
    start_time = time.time()
    executor = cf.ThreadPoolExecutor()
    wait_for = [executor.submit(load_page, url) for url in URLS]
    for f in cf.as_completed(wait_for): #迭代完成的任务，输出其结果
        print(f.result())
    end_time = time.time()
    print("并发处理消耗时间：{}".format(end_time - start_time))
