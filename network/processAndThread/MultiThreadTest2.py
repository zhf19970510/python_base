import time
from threading import Thread

# 第二种方式创建多线程
class EatThread(Thread):
    """
    写一个自定义的类继承Process
    """

    def __init__(self, name):
        super().__init__()  # 注意：这行代码必须要有
        self.name = name

    def run(self):
        for i in range(6):
            print(f'进程{self.name}正在吃饭...')
            time.sleep(0.3)


class WorkThread(Thread):
    """
    写一个自定义的类继承Process
    """

    def __init__(self, name):
        super().__init__()  # 注意：这行代码必须要有
        self.name = name

    def run(self):
        for i in range(6):
            print(f'进程{self.name}正在做作业...')
            time.sleep(0.3)


if __name__ == '__main__':
    p1 = EatThread('t-1')
    p2 = WorkThread('t-2')

    p1.start()
    p2.start()