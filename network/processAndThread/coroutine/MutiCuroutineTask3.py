import asyncio
import time


async def eat():
    for i in range(6):
        print('正在吃饭')
        await asyncio.sleep(0)      # 目的：切换


# 做作业任务
async def work():
    for i in range(6):
        print('正在做作业')
        await asyncio.sleep(0)      # 目的：切换


async def main():       # 其他协程的入口
    task1 = asyncio.create_task(eat())
    task2 = asyncio.create_task(work())
    # 虽然这样看着是同步的写法，但是由于被包装成异步任务了，所以这里的结果还是异步的
    # await task1
    # await task2
    # 这里也可以使用gather的写法
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'耗时:{time.time() - start}')