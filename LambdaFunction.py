"""
如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化
lambda 参数列表 : 表达式

注意：
lambda表达式的参数可有可无
lambda表达式能接收任何数量的参数但只能返回一个表达式的值
直接打印lambda表达式，输出的是此lambda的内存地址
"""

fn1 = lambda a, b: a + b
fn2 = lambda a, b: a - b
fn3 = lambda a, b: a * b
fn4 = lambda a, b: a / b
fn5 = lambda a, b: a // b
fn6 = lambda a, b: a % b

print(fn1(1, 2))
print(fn1)


# 给某个复杂的列表排序
lst = [
    {'name': '张三', 'age': 34},
    {'name': '李四', 'age': 16},
    {'name': '王五', 'age': 41},
]

# 根据年龄排序
sorted_lst = sorted(lst, key=lambda k: k['age'])
print(sorted_lst)
print(lst)
# sorted 不会修改lst的顺序，可以通过lst.sort来修改原有列表的顺序
lst.sort(key=lambda k: k['age'])
print(lst)
# 也可以指定排序的顺序
lst.sort(key=lambda k: k['age'], reverse=True)
print(lst)