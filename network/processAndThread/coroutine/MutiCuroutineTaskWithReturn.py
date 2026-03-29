import asyncio
import time


async def eat():
    for i in range(6):
        print('正在吃饭')
        await asyncio.sleep(0)      # 目的：切换

    return '吃饭完成'


# 做作业任务
async def work():
    for i in range(6):
        print('正在做作业')
        await asyncio.sleep(0)      # 目的：切换
    return '做作业完成'


async def main():       # 其他协程的入口
    task1 = asyncio.create_task(eat())
    task2 = asyncio.create_task(work())
    # 虽然这样看着是同步的写法，但是由于被包装成异步任务了，所以这里的结果还是异步的
    # await task1
    # await task2
    # 这里也可以使用gather的写法
    # result = await asyncio.gather(task1, task2)     # 仅仅得到函数的返回值，当第一个携程 task1.cancel() 强制终止了，会影响第二个协程，可以增加参数：return_exceptions=True
    # await asyncio.gather(task1, task2, return_exceptions=True)    # 这样不会影响到第二个协程运行

    # 得到更加详细的返回信息
    # result = await asyncio.wait([task1, task2])     # 可以得到任务的详细信息，包括返回值

    # 指定某一个任务结束后就返回，默认：return_when=asyncio.ALL_COMPLETED
    result = await asyncio.wait([task1, task2], return_when=asyncio.FIRST_COMPLETED)     # 可以得到任务的详细信息，包括返回值
    print(result)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'耗时:{time.time() - start}')