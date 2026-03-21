"""
递归函数
"""


def test(n: int) -> int:
    """
    计算一个数字n的阶乘
    :param n:
    :return:
    """
    if n == 1:
        return 1        # 这就是递归函数的出口
    return n * test(n - 1)


print(test(6))