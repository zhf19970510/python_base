"""
1. 类函数
需要用装饰器 @clssmethod 来标识为类函数，对于类函数，第一个参数必须是类（当前类），一般以cls作为第一个参数。
但是：也可以命名其他的。一般习惯上都用cls

2. 静态函数
需要通过装饰器 @staticmethod 来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）。
静态方法也能通过 实例对象 和 类对象 去访问
特点：
既不需要使用实例对象，也不需要使用类对象定义静态方法
取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
"""


class Person():
    def __init__(self, name):  # 成员函数，对象函数，实例函数
        self.name = name

    def eat(self):  # 成员函数，对象函数，实例函数
        print(f'{self.name} 正在吃饭')

    @classmethod
    def work(cls, other, num=100):  # 类函数
        print(cls.__name__, other, num)
        print('每个人都要工作')

    @staticmethod
    def run():
        print('每个人都可以跑起来')

p1 = Person('张三')
p1.eat()
p1.work('abc')
Person.work('cfg')

# 静态函数调用：两种方法
p1.run()
Person.run()