"""
asyncio是用来编写协程代码库的，使用async/await语法，被用作多个提供高性能Python异步框架的基础

async关键字定义的函数就是异步函数，也可理解为：定义一个协程。异步函数的实例化对象就是一个协程。

启动多协程任务：
asyncio.run(coro, *, debug=False)) 函数用来运行最高层级的入口点 "test1()" 函数
"""
import asyncio
import time


def hello(msg: str):
    print(f'hello {msg}')

# 定义一个异步函数
async def test1():
    print('hello')
    # 挂起当前的协程序，等待1秒钟。
    # 当该协程挂起的时候，可以去执行其他的协程（异步任务）
    await asyncio.sleep(1)      # 目的：切换
    # time.sleep(1)                # 不会进行协程的切换，只会让当前线程挂起，并且等待1s
    print('world')

hello('zhf')


# 启动所有协程
# test1() 是为了得到一个协程，真正启动协程要用 asyncio.run
# coroutine1 = test1()
# asyncio.run(coroutine1)

# 简化写法
asyncio.run(test1())