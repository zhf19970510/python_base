class Animal:
    def say(self):
        pass


class Dog(Animal):
    def say(self):
        print('旺旺')

class Cat(Animal):
    def say(self):
        print('喵喵')


def test(obj: Animal):
    obj.say()

d = Dog()
test(d)
d = Cat()
test(d)