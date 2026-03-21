"""
高阶函数
把函数作为参数传入，或者返回值是另外一个函数，这样的函数称为高阶函数，高阶函数是函数式编程的体现。
函数式编程就是指这种高度抽象的编程范式。
函数式编程大量使用函数，减少了代码的重复，因此程序比较短，开发速度比较快

"""


# 对任意两个数字，整理之后再求和
def sum_num(a, b):
    return abs(a) + abs(b)


# 高阶函数实现
def sum_num2(a, b, f):
    """
    :param a:
    :param b:
    :param f:   对两个变量进行整理的函数
    :return:
    """
    return f(a) + f(b)


def my_bas(x):
    return abs(x)


print(sum_num2(-2, -3, abs))

print(sum_num2(-3, -4, lambda k: abs(k)))

print(sum_num2(-4, -5, my_bas))

print(sum_num2(-2, -6, lambda n: n ** 2))

"""
函数的返回值是函数
高阶函数除了可以接收函数作为参数外，还可以把函数作为结果值返回
一个函数返回值(return)为另一个函数
"""
print('-' * 50)


def sum_fun_b(*args):
    def sum_a():
        a = 0
        for n in args:
            a += n
        return a

    return sum_a


f = sum_fun_b(1, 2, 3)
print(f())

"""
Python中内置的高阶函数

一、map函数
map函数接收的是两个参数：一个是函数名，另外一个是序列，其功能是将序列中的数值作为函数的参数依次传入到函数中执行，然后再返回到列表中
返回值是一个迭代器对象

二、reduce函数
reduce函数也是一个参数为函数，另一个参数为序列对象（比如：list列表）。其返回值为一个值而不是迭代器对象，故其常用于叠加，叠乘等等。

三、filter函数
Python内建的filter()函数用于过滤序列，和map类似，filter()也接收一个函数和序列；但不同的是filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定元素的保留与丢弃

四、sorted函数
Python内置的sorted()函数可以对list进行排序；和序列中本身的sort函数类似
"""
print('-' * 25 + 'map函数' + '-' * 25)
lst = [1, 2, 3, 4, 5]
for e in map(lambda x: x ** 2, lst):
    print(e)

print('-' * 50)


def square(x):
    return x ** 2


for e in map(square, lst):
    print(e)

print(list(map(square, lst)))

print('-' * 25 + 'reduce函数' + '-' * 25)
"""
reduce函数
一个参数为函数，另一个参数为序列对象（比如：list列表）。其返回值为一个值而不是迭代器对象，故常用于叠加、叠乘等等。
函数详解：
1. function: 一个有两个参数的函数
2. sequence: 是一个序列，是一些数据的集合，或者一组数据，可迭代对象
3. initial: 可选，初始参数
4. 返回值: 返回函数计算结果
5. reduce()函数，使用function函数（有两个参数）先对集合中的sequence第1、2个元素进行操作，如果存在initial参数，
则将会以sequence中的第一个元素和initial作为参数，用作调用，得到的结果再与sequence中下一个数据用function函数运算，
最后得到一个结果
"""

from functools import reduce

list_a = [1, 2, 3, 4, 5]


def fun_b(x, y):
    return x + y


print(reduce(lambda x, y: x + y, [2, 4, 6, 8, 10]))

print(reduce(fun_b, list_a))
print(reduce(fun_b, list_a, 100))

# 案例：给你很长的字符串，统计字符串中每个单词出现的次数
str1 = 'hello world python hello python java hello python flask'
# 第一步，把单词切开
lst = str1.split(' ')
# 第二步，每个单词出现了，那么就代表有一次
new_lst = list(map(lambda x: {x: 1}, lst))
print(new_lst)


# 第三步，调用reduce，实现相同单词的叠加
def func(dict1, dict2):
    # 把dict1作为叠加的返回字典
    key = list(dict2.items())[0][0]  # 得到dict2中的key
    value = list(dict2.items())[0][1]  # 得到dict2中的value
    dict1[key] = dict1.get(key, 0) + value
    return dict1


print(reduce(func, new_lst))

print(reduce(func, map(lambda x: {x: 1}, str1.split(' '))))

"""
filter函数
"""
print('-' * 25 + 'filter函数' + '-' * 25)

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 偶数留下
new_lst = list(filter(lambda x: x & 1 == 0, lst1))
print(new_lst)


"""
sorted函数
"""
print('-' * 25 + 'sorted函数' + '-' * 25)
# 给某个复杂的列表排序
lst = [
    {'name': '张三', 'age': 34},
    {'name': '李四', 'age': 16},
    {'name': '王五', 'age': 41},
]

# 根据年龄排序
sorted_lst = sorted(lst, key=lambda k: k['age'])
print(sorted_lst)
print(lst)
# sorted 不会修改lst的顺序，可以通过lst.sort来修改原有列表的顺序
lst.sort(key=lambda k: k['age'])
print(lst)
# 也可以指定排序的顺序
lst.sort(key=lambda k: k['age'], reverse=True)
print(lst)

str_lst = ['hello', 'Java', 'Zoo', 'world']
print(sorted(str_lst))  # 默认情况下，对字符串排序，是按照ASCII的大小比较的

print(sorted(str_lst, key=lambda s: s.lower()))