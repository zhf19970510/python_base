import asyncio

async def eat():
    for i in range(6):
        print('正在吃饭')
        await asyncio.sleep(0.5)      # 目的：切换


# 做作业任务
async def work():
    for i in range(6):
        print('正在做作业')
        await asyncio.sleep(0.5)      # 目的：切换


async def main():       # 其他协程的入口
    await eat()
    await work()        # 这里这两个协程没有达成协作，结果是同步执行的

if __name__ == '__main__':
    asyncio.run(main())