from typing import Iterator


class MyRange(object):
    """range(6),从0开始，一直到6（不包括6）"""

    def __init__(self, stop_num):
        self.stop_num = stop_num  # 结束数字（不包括）
        self.num = -1

    def __iter__(self):
        print('__iter__')
        return self
        return self

    def __next__(self):
        print('__next__')
        self.num += 1
        if self.num >= self.stop_num:
            raise StopIteration
        return self.num


if __name__ == '__main__':
    obj = MyRange(6)
    print(isinstance(obj, Iterator))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))
    # print(next(obj))

    """
    for 循环本质：
    1. 使用iter获得可迭代对象的迭代器
    2. 反复对迭代器使用next函数
    3. 捕获StopIteration异常，退出循环
    """
    for item in obj:
        print(f'迭代器对象中的值：{item}')