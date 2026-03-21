"""
私有属性和函数：
在Python中，可以为属性和函数设置私有权限，即设置某个属性或函数不继承给子类。甚至，不能在类的外部调用和访问

设置私有权限的方法：在属性名和函数名 前面 加上两个下划线：__

如果也想要别人去访问和修改私有属性：在Python中，一般定义函数名 get_xx用来获取私有属性，定义 set_xx 用来修改私有属性值。
"""

class Animal(object):

    __name = '动物'   # 私有属性（类属性）

    def __init__(self, color):
        self.__color = color  # 私有属性


    def __run(self):    # 私有函数
        print(self.__name)  # 在类的内部可以访问私有属性
        print('动物跑起来')

    def say(self):
        print('动物喊叫')

    def set_color(self, new_color):     # 通过提供一个set函数来修改私有属性
        self.__color = new_color

    def get_color(self):
        return self.__color

class Dog(Animal):
    pass

d = Dog('red')
# d.__run()   # 会报错
# d.__name    # 会报错
d.set_color('green')
print(d.get_color())