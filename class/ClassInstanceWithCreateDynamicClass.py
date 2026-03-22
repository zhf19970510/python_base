"""
1)使用函数的方式来定义一个元类

需求：动态改变类中所有属性名都改成大写，类的私有属性除外

"""

def UpperMetaCase(class_name, class_parents, class_attrs):
    new_attrs = {}
    for name, value in class_attrs.items():
        if not name.startswith('_'):
            new_attrs[name.upper()] = value
        else:
            new_attrs[name] = value
    return type(class_name, class_parents, new_attrs)

class Person(object, metaclass=UpperMetaCase):

    name = 'zhangsan'
    age = 21


if __name__ == '__main__':
    Person.age = 33
    Person.attr1 = 222
    print(Person.attr1)
    print(Person.age)
    'abc'.startswith('abc')
    p = Person()
    print(p.attr1)
    p.name111 = '张三'
    print(p.name111)