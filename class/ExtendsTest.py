"""
Python面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和函数。
在Python中，所有类默认继承object类，object类是顶级类或基类
"""

class Animal:
    name = '动物'

    def say(self):
        print('动物的叫声')

class Dog(Animal):  # 子类只继承一个父类，单继承

    def see_home(self):
        print('狗可以看家护院')


d = Dog()
d.say()
print(d.name)
d.see_home()


# 子类的对象 是子类类型，同时也是父类类型
print(type(d))
print(isinstance(d, Dog))
isInstance = isinstance(d, Animal)
print(isInstance)

issubclass = issubclass(Dog, Animal)
print(issubclass)
