class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        print('调用了age函数')
        return self.__age

    @age.setter     # 该装饰器把age当成属性了，但是只能用于给age赋值
    def age(self, x_age):
        print('调用了设置__age的函数')
        self.__age = x_age

if __name__ == '__main__':
    person = Person(age=20)
    person.age = -10
    print(person.age)