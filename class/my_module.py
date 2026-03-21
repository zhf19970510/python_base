def my_sum(n):
    """
    计算从0到n的数字之和
    :param n: 正整数
    :return:
    """
    s = 0
    for i in range(n):
        s += i
    return s


def test(n: int) -> int:
    """
    计算一个数字n的阶乘
    :param n:
    :return:
    """
    if n == 1:
        return 1  # 这就是递归函数的出口
    return n * test(n - 1)

if __name__ == '__main__':
    print(my_sum(8))
    print(test(6))
