"""
必要参数，也叫位置参数
定义函数时，根据需求必须要传递的参数，而且，在调用函数时根据函数定义的参数位置顺序来传递参数
注意：传递和定义参数的顺序及个数必须一致

关键字传参：
函数调用，通过"键=值"形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求
注意：函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序。

默认参数：
用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和使用）。

不定长传参：
不定长参数也叫可变参数。用于不确定调用的时候会传递多少个参数（不传参也可以）的场景。此时来进行参数传递，会显得非常方便
1. 不定长普通参数
2. 不定长关键字参数
"""


def test1(x, y):
    return x + y


print(test1(1, 2))

print(test1(y=10, x=20))


# 默认值参数

def test2(x, y, init_sum = 10):
    return x + y + init_sum


print(test2(10, 20))
print(test2(10, 20, init_sum = 30))

# 不定长参数
def test3(*args, init_sum = 10):
    print(type(args))
    if args:
        for arg in args:
            init_sum += arg
    return init_sum

print(test3())
print(test3(1))
print(test3(10, 20, init_sum = 30))

# test3 函数优化
def test4(*args, init_sum = 10):
    print(type(args))
    if args:
        return init_sum + sum(args)
    return init_sum

print(test4())
print(test4(1))
print(test4(10, 20, init_sum = 30))


# 不定长关键字参数

def test5(init_sum = 10, **kwargs):
    print(type(kwargs))
    if kwargs:
        for key, value in kwargs.items():
            init_sum += value
            print(f'参数的名字{key}, 参数的值{value}')
    return init_sum


def test6(init_sum = 10, **kwargs):
    print(type(kwargs))
    if kwargs:
        return init_sum + sum(kwargs.values())
    return init_sum

test5(x = 10, y = 20, z = 30)
test5(x = 10, y = 20, z = 30, init_sum = 30)


# 参数顺序，位置参数 -> 默认传参 -> 不定长普通参数 -> 不定长关键字参数

def test7(a, b, c = 100, * args, ** kwargs):
    pass