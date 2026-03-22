
class SinglePerson(object):

    def __new__(cls, *args, **kwargs):
        # 采用私有属性，单下划线开头，可以被子类继承。在import导入中，不会导入单下划线的私有属性
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == '__main__':
    p1 = SinglePerson()
    p2 = SinglePerson()

    print(id(p1), id(p2))

    print(p1 is p2)
    print(p1 == p2)