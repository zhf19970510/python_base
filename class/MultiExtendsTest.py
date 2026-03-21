"""
在python中是可以多继承的，继承的先后顺序是有区别的，当我们调用函数的时候，如果第一个继承的找不到，才会去第二个中找
但是只要在第一个类中找到调用的那个函数，即使参数个数不匹配也不会调用第二个父类中的，此时会报错
MRO顺序：Python官方采用了一个算法将复杂结构上所有的类全部映射到一个线性顺序上，而根据这个顺序就能保证所有的类都会被构造一次
"""
class Parent:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        print('parent的init函数被执行了')


    def test1(self):
        print('parent的test函数被执行了')

class Son1(Parent):

    def __init__(self, name, age, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.age = age
        print('son1的init函数被执行了')

    def test1(self):
        print('son1的test函数被执行了')


class Son2(Parent):

    def __init__(self, name, sex, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.sex = sex
        print('son2的init函数被执行了')

    def test1(self):
        print('son2的test函数被执行了')

class GrandSon(Son1, Son2):

    def __init__(self, name, age, sex,  *args, **kwargs):
        super().__init__(name, age, sex)
        print('GrandSon的init函数被执行了')

print(f'MRO序列是：{GrandSon.__mro__}')
gs = GrandSon('zhangsan', 34, '男')
gs.test1()