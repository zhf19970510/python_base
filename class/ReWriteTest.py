class Parent:

    def __init__(self, name):
        self.name = name
        print('parent的init被执行了')

    def say_hello(self):
        print(f'{self.name}: hello')
        print('parent的say_hello被执行了')


class Son(Parent):

    def __init__(self, name, age):
        print('son的init函数被执行了')
        super().__init__(name)
        self.age = age

    def say_hello(self):
        print(f'{self.name}: hello')
        print('son的say_hello被执行了')

s1 = Son('张三', 18)
s1.say_hello()
print(s1.age)