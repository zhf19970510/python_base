from threading import Thread, Lock

g_num = 0

lock = Lock()   # 创建锁

def sum_num1():
    with lock:
        global g_num
        for i in range(1000000):
            g_num += 1
    print(f'线程1累加之后的结果：{g_num}')


def sum_num2():
    with lock:
        global g_num
        for i in range(1000000):
            g_num += 1
    print(f'线程2累加之后的结果：{g_num}')


if __name__ == '__main__':
    t1 = Thread(target=sum_num1)
    t2 = Thread(target=sum_num2)

    t1.start()
    t2.start()