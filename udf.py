# 自定义函数，函数必须先定义后使用
def my_abs(num):
    """
    该函数，可以返回一个数字的绝对值
    :param num: 传入的数字，必须是个数字，而且必传
    :return: 返回该数字的绝对值
    """
    if num < 0:
        return -num
    else:
        return num


# 在python 3.5 之后，可以对函数参数和返回值进行类型的声明
print(my_abs(-100))
# print(my_abs('abc'))

def new_abs(num: int) -> int:
    """
    该函数，可以返回一个数字的绝对值
    :param num: 传入的数字，必须是个数字，而且必传
    :return: 返回该数字的绝对值
    """
    return abs(num)

print(new_abs(-100))
# print(new_abs('abc'))   # 此行代码会有黄色警告，因为函数定义要求传入参数是int类型
