import concurrent.futures
import urllib.request
import time
def load_url(url, timeout):
    """读取指定url的网页数据"""
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()
if __name__ == '__main__':
    #测试数据，gutenberg网站TOP 9 Ebooks
    URLS = {'Pride and Prejudice': 'http://www.gutenberg.org/files/1342/1342-0.txt',
            'Heart of Darkness': 'http://www.gutenberg.org/files/219/219-0.txt',
            'Moby Dick': 'http://www.gutenberg.org/files/2701/2701-0.txt',
            'Frankenstein': 'http://www.gutenberg.org/files/84/84-0.txt',
            'Manual of Classical Erotology': 'http://www.gutenberg.org/files/57284/57284-0.txt',
            'A Tale of Two Cities': 'http://www.gutenberg.org/files/98/98-0.txt',
            'Alice Adventures in Wonderland': 'http://www.gutenberg.org/files/11/11-0.txt',
            'The Adventures of Tom Sawyer': 'http://www.gutenberg.org/files/74/74-0.txt',
            'Grimms Fairy Tales': 'http://www.gutenberg.org/files/2591/2591-0.txt'}
    # 串行处理测试
    start_time = time.time()  # 结束时间
    for name, url in URLS.items():
        data = load_url(url, 60)
        with open("{}.txt".format(name), 'wb') as f:  # 保存下载的文件
            f.write(data)
        print('下载{}完成，文件大小为{}字节'.format(name, len(data)))
    end_time = time.time()
    print("串行处理消耗时间：{}".format(end_time - start_time))
    # 并行处理测试
    start_time = time.time()  # 开始时间
    #使用上下文创建线程池执行器，以确保其关闭
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        #使用ThreadPoolExecutor调度任务
        future_to_name = {executor.submit(load_url, url, 60): name for name, url in URLS.items()}
        #迭代已完成的任务，并输出结果
        for future in concurrent.futures.as_completed(future_to_name):
            name = future_to_name[future]
            try:
                data = future.result()
            except Exception as exc:
                print('下载{}时出错{}'.format(name, exc))
            else:
                with open("{}.txt".format(name), 'wb') as f: #保存下载的文件
                    f.write(data)
                print('下载{}完成，文件大小为{}字节'.format(name, len(data)))
    end_time = time.time()
    print("并行处理消耗时间：{}".format(end_time - start_time))
