"""
Queue([maxsize]):建立一个共享的队列（内部维护着数据的共享），多个进程可以向队列里存/取数据。其中，参数是队列最大项数，省略则无限制
"""
import time
from multiprocessing import Pool, Process, Queue


# 创建进程执行多任务

def add_data(q: Queue):
    for i in range(6):
        q.put(i)
        time.sleep(0.3)


def read_data(q: Queue):
    while True:
        # get函数是一个阻塞的函数，get函数是从队列中获取一个值，并且这个值从队列中删除
        value = q.get()
        print(value)
        time.sleep(0.4)


if __name__ == '__main__':
    q = Queue(100)

    p1 = Process(target=add_data, args=(q,))  # 往队列中存放数据的进程
    p2 = Process(target=read_data, args=(q,))  # 往队列中获取数据
    p1.start()
    p2.start()
    p1.join()
