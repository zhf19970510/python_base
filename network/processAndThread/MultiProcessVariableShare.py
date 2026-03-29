"""
多进程之间是否可以通过定义一个全局变量来共享变量
"""
import time
from multiprocessing import Pool, Process

my_list = []

# 创建进程执行多任务

def add_data():
    for i in range(6):
        my_list.append(i)
        time.sleep(0.3)
    print(my_list)


def read_data():
    print(my_list)

if __name__ == '__main__':
    p1 = Process(target=add_data)
    p2 = Process(target=read_data)
    p1.start()

    p1.join()

    # 这里会发现 read_data 函数并没有打印my_list,原因就是多进程之间不能共享变量
    p2.start()
    # 怎么解决进程之间变量共享的问题？进行通信


