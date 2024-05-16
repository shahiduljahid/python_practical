import asyncio, time
async def do_some_work(n): #使用async关键字定义异步函数
    print('等待:{}秒'.format(n))
    await asyncio.sleep(n)  #休眠一段时间
    return '{}秒后返回结束运行'.format(n)
start_time = time.time() #开始时间
coro = do_some_work(2)
loop = asyncio.get_event_loop()
loop.run_until_complete(coro)
print('运行时间: ', time.time() - start_time)
