"""
2）采用类的方式定义元类
"""
class UpperMetaClass(type):

    # 如果需要，重新创建Person类对象，需要重写 __new__
    def __new__(cls, class_name, class_parents, class_attrs):
        new_attrs = dict(((name, value) if name.startswith('__') else (name.upper(), value) for name, value in class_attrs.items()))
        return super().__new__(cls, class_name, class_parents, new_attrs)

class Person(object, metaclass=UpperMetaClass):

    name = 'zhangsan'
    __age = 21

if __name__ == '__main__':
    print(Person.NAME)
    print(hasattr(Person, 'NAME'))
    print(hasattr(Person, 'name'))
    print(hasattr(Person, '__age'))
    print(hasattr(Person, '__age'))
    print(hasattr(Person, '_Person__age'))
    print(dir(Person))