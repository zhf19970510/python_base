from iterator_test.IteratorTest import MyRange


class ItRange(object):
    """自定义可迭代对象"""

    def __iter__(self):
        return MyRange(6)