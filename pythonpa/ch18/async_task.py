import asyncio, time
async def do_some_work(i, n): #使用async关键字定义异步函数
    print('任务{}等待: {}秒'.format(i, n))
    await asyncio.sleep(n)  #休眠一段时间
    return '任务{}在{}秒后返回结束运行'.format(i, n)
start_time = time.time() #开始时间
tasks = [asyncio.ensure_future(do_some_work(1, 2)),
        asyncio.ensure_future(do_some_work(2, 1)),
        asyncio.ensure_future(do_some_work(3, 3))]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print('任务执行结果: ', task.result())
print('运行时间: ', time.time() - start_time)
