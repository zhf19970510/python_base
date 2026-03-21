"""
类属性和实例属性
类属性：就是类所拥有的属性，它被该类的所有实例所共有
实例属性：就是单个对象或者实例才拥有的属性
"""

class Person():

    species = '人类'      # 物种的名字，是类属性

    def __init__(self, name):
        self.name = name    # 对象属性，成员属性，    实例属性

    def setName(self, name):
        self.name = name

p1 = Person('张三')
p2 = Person('李四')

print(p1.species)
print(p2.species)

# 访问属性（类属性、对象属性）
print(p1.name)
print(p2.name)
print(p1.species)
print(Person.species)

# 修改属性
p1.name = 'zhangsan'
print(p1.name)
print(p2.name)

# 修改类属性只有一种方法
p1.species = 'abc'      # 这里并不是修改类属性，而是增加了一个对象属性
print(p1.species)
print(p2.species)
print(Person.species)   # 实际没有改，所以类属性只能通过类名.属性名进行修改

Person.species = 'def'
print(p1.species)
print(p2.species)
print(Person.species)