"""
可变类型和不可变类型
字符串str: 储存字符编码值，不可变，序列
列表list: 存储变量，可变，序列
元组tuple: 储存变量，不可变，序列
字典dict: 储存键值对，可变，散列，键不能重复且不可变
集合set: 储存键，可变，散列
"""

s1 = "helloworld!"
print(id(s1))   # 打印内存地址
print(s1)
s1 = 'abc'
print(id(s1))
print(s1)

print('-' * 50)

lst = [100, 200, 400]
print(id(lst))
lst.append(500)
lst.pop(1)
print(id(lst))
print(lst)
