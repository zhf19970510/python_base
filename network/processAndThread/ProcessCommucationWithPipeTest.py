"""
进程间通信基于管道（Pipe）实现

如果你创建了很多个子进程，那么其中任何一个子进程都可以对Queue进行存(put)和取(get)。
但Pipe不一样，Pipe只提供两个端点，只允许两个进程进行存(send)和取(recv)。
也就是说，Pipe实现了两个子进程之间的通信
"""
import time
from multiprocessing import Process, Pipe


# 创建进程执行多任务

def add_data(pi: Pipe):
    for i in range(6):
        pi.send(f'数据{i}')
        time.sleep(0.3)


def read_data(pi: Pipe):
    while True:
        # recv函数是一个阻塞的函数，
        value = pi.recv()
        print(value)
        time.sleep(0.4)


if __name__ == '__main__':
    # 创建一个管道，需要两个端点
    send_pi, recv_pi = Pipe()

    p1 = Process(target=add_data, args=(send_pi,))  # 往队列中存放数据的进程
    p2 = Process(target=read_data, args=(recv_pi,))  # 往队列中获取数据
    p1.start()
    p2.start()
    p1.join()
