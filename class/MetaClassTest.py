"""
type就是Python在背后用来创建所有类的元类
1. type可以创建类
2. type创建的对象拥有创建对象的能力（也就是类）
3. type就是Python中所有类的元类（metaclass）


元类就是用来创建这些类（对象）的，元类就是创建类的类。元类并不是某一个类的名字，它是一个概念，是一种Python思想。它可以帮我们动态地创建类

使用元类动态创建类： 参考ClassInstanceWithCreateDynamicClass.py

结合ClassInstance.py一起看
"""
# class Person(object, metaclass=type): # metaclass = type 是隐藏逻辑
class Person(object):
    age = 33

if __name__ == '__main__':
    # python解释器 怎么创建一个类对象的

    # c1 就是一个类对象
    c1 = Person

    # 手动创建一个类对象，模拟python解释器创建类对象的过程
    c2 = type('Person', (object,), {'age': 3})

    print(c1.age)
    print(c2.age)
    print(c1.age)
    print('-' * 50)

    # 通过类对象创建一个实例对象
    p1 = c1()
    p2 = c2()
    print(p1.age)
    print(p2.age)
    print(p1.__class__)
    print(p2.__class__)
