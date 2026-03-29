from threading import Thread

g_num = 0

# 需求：采用两个线程，分别对 g_num 累加100万次

# 在该案例中无法保证线程安全，因为两个线程同时操作全局变量，既没有用join，也没有用互斥锁

def sum_num1():
    global g_num
    for i in range(1000000):
        g_num += 1
    print(f'线程1累加之后的结果：{g_num}')


def sum_num2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print(f'线程2累加之后的结果：{g_num}')


if __name__ == '__main__':
    t1 = Thread(target=sum_num1)
    t2 = Thread(target=sum_num2)

    t1.start()
    t2.start()