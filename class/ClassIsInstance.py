"""
在Python中有两种对象：
类型（类）对象：可以被实例化和继承；Person
非类型（实例）对象：不可以被实例和继承。P = Person()

type为对象的顶点，所有对象都创建自type
object为类继承的顶点，所有类都继承自object

type元类：
type:
int、function、自定义类、python其他的内置类都是由元类创建的
就像str是用来创建字符串对象的类，int是用来创建整数对象的类，而type就是创建类对象的类

结合MetaClassTest.py一起看
"""

class Person(object):
    pass

if __name__ == '__main__':
    p = Person()    # 基于类对象创建了一个实例对象
    # p是实例对象
    print(f'p这个对象是由：{p.__class__} 这个类对象创建的')
    # print(f'这个对象的父对象是：{}')

    # Person对象
    print(f'Person这个对象的父对象是：{Person.__base__}')
    print(f'Person这个对象是由：{Person.__class__} 这个类对象创建的')


    # Person对象
    print(f'int这个对象的父对象是：{int.__base__}')
    print(f'int这个对象是由：{int.__class__} 这个类对象创建的')


    # Person对象
    print(f'str这个对象的父对象是：{str.__base__}')
    print(f'str这个对象是由：{str.__class__} 这个类对象创建的')