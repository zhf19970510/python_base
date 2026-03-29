"""
语法：Pool([numProcess[,initializer [,initargs]]])  # 创建进程池

参数介绍：
numprocess: 要创建的进程数，如果省略，将默认使用cpu_count()的值
initializer: 是每个工作进程启动时要执行的可调用对象，默认None  - 一般不需要传入
initargs: 是要传给initializer的参数组   - 一般不需要传入
"""
import time
from multiprocessing import Pool


# 创建进程执行多任务

# 吃饭任务
def eat(name):
    for i in range(6):
        print(f'正在吃饭...{name}')
        time.sleep(0.3)


# 做作业任务
def work():
    for i in range(6):
        print('正在做作业...')
        time.sleep(0.3)


# 打游戏任务
def game():
    for i in range(6):
        print('正在打游戏...')
        time.sleep(0.3)


if __name__ == '__main__':
    process_pool = Pool(3)

    # apply 函数式一个阻塞的函数（主进程阻塞）
    # process_pool.apply(eat, args=('张三',)) # 从进程池中申请一个新的进程去执行eat
    # process_pool.apply(work)

    # async: 异步调用（非阻塞）
    process_pool.apply_async(eat, args=('张三',))
    process_pool.apply_async(work)

    # 进程池关闭，进程池不再接收新的请求
    process_pool.close()

    # process_pool.apply_async(game)

    # 采用进程池的异步调用，主进程默认是不会等待所有的子进程执行完成的
    process_pool.join()
