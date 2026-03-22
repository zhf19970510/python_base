import time

def timer(func):
    def inner():
        start = time.time()
        result = func()
        end = time.time()
        print(f'函数{func.__name__}执行的时间是：{end-start}')
        return result
    return inner


@timer
def test1():
    print('test1')
    time.sleep(1)

@timer
def test2():
    print('test1')
    time.sleep(3)

if __name__ == '__main__':
    test1()
    test2()