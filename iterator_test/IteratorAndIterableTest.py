"""
1. 迭代器对象
定义：
1. 类中定义了__iter__和__next__函数
2. __iter__函数返回self，也就是自身
3. __next__函数返回下一个数据，如果没有数据了，则要返回StopIteration的异常
满足这三个条件的对象，就是迭代器对象

2. 可迭代对象
定义：如果一个类中包含__iter__函数，并且返回一个迭代器，则称这个类创建的对象为可迭对象。所以：迭代器对象也是可迭代对象。
"""


from typing import Iterable

from IteratorTest import MyRange
from iterator_test.CouldIteratorObj import ItRange

if __name__ == '__main__':
    # MyRange是迭代器对象
    obj1 = MyRange(10)
    obj2 = range(10)
    obj3 = obj2.__iter__()  # 返回迭代器对象
    obj4 = ItRange()

    # obj2 和 obj4 是可迭代对象
    print(isinstance(obj2, Iterable))
    print(isinstance(obj4, Iterable))

    print(dir(obj1))
    print(dir(obj2))
    print(dir(obj3))

    # 列表也是可迭代对象
    obj5 = [1, 2, 3, 4]
    print(dir(obj5))
    print(isinstance(obj5, Iterable))

    # 所有的可迭代对象和迭代器对象，都可通过for循环遍历

    """
    什么是迭代器和可迭代对象，他们之间有什么关系？
    1. 迭代器：如果一个对象同时实现了__iter__函数和__next__函数，它就是迭代器对象
    2. 可迭代对象：如果一个对象实现了__iter__函数，那么这个对象就是可迭代对象
    3. 他们之间有什么关系：迭代器一定是可迭代对象，反之则不成立，可迭代对象的__iter__函数必须返回一个迭代器
    
    迭代器优点：
    1. 提供了一种通用的不依赖索引的迭代取值方式；
    2. 节省内存，迭代器在内存中相当于只占用一个数据的空间：因为每次取值上一条数据会在内存中释放，加载当前的此条数据
    
    迭代器缺点：
    1. 因为有next函数，即只能往后取值，不能往前，取值不如按照索引的方式灵活，不能指定某一个值
    2. 无法预测迭代器的长度
    
    """