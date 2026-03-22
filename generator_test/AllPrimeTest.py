

def generator_func():
    """生成所有的质数"""
    i = 2
    yield i
    while True:
        i += 1
        # 判断i是否是质数
        end = (int) (i >> 1) + 1
        for j in range(2, end):
            if i % j == 0:  # 可以被其他数字整除，所以不是i不是质数
                break
        else:   # 数字i不可以被其他数字整除
            yield i



if __name__ == '__main__':
    g = generator_func()
    num = next(g)
    while num <= 100:
        print(num)
        num = next(g)