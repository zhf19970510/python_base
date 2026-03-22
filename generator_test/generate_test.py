
"""
生成器也是一个迭代器

生成器是一个包含yield关键字的函数，当它被调用时，在函数体内的代码不会被执行，而是返回一个迭代器，每次请求一个值，
就会执行生成器的代码，直到遇到一个yeld或者return语句。yield语句意味着生成一个值，return语句要求停止执行（不再生成任何东西）

总结：
1. yield把函数变成了一个生成器
2. 调用该函数不会立即执行代码，而是返回了一个生成器对象
3. 当使用next()（在for循环中会自动调用next()）作用于返回的生成器对象时，函数开始执行，在遇到yield的时候会【暂停】，并返回当前的迭代值
4. 当再次调用next()的时候，函数会从原来【暂停】的地方继续执行，直到遇到yield语句，如果没有yield语句，则抛出异常；
5. 生成器函数的执行过程看起来就是不断地=执行>中断>执行>中断的过程
6. send()函数就是next()的功能，加上传值给上次暂停的yield
7. close()函数来关闭一个生成器。生成器被关闭后，再次调用next()函数，不管能否遇到yield关键字，都会抛出StopIteration异常
"""
from typing import Iterator


def generator_func():
    v1 = yield 1
    print(f'第一次传给生成器的值是：{v1}')
    v2 = yield 2
    print(f'第二次传给生成器的值是：{v2}')
    print('hello')
    v3 = yield 3
    print(f'第三次传给生成器的值是：{v3}')
    v4 = yield 4
    print(f'第四次传给生成器的值是：{v4}')

g = generator_func()    # 创建了一个生成器

print(isinstance(g, Iterator))

print(hasattr(g, '__iter__'))   # 判断对象g中，是否包含__iter__的函数
print(hasattr(g, '__next__'))   # 判断对象g中，是否包含__next__的函数

# 连续从生成器中取3个值
# print(next(g))
# print(next(g))
# print(next(g))

# 还可以通过send函数，把值传给生成器
print(next(g))
print(g.send(100))
print(g.send(200))
print(g.send(300))

