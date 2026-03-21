"""
函数的返回值：
return语句用于返回函数的值，并且退出函数，选择性地使用return语句，默认是返回None

1. return a,b写法：返回多个数据的时候，默认是元组类型。
2. return后面可以连接列表，元组或字典，以返回多个值
"""

def test1():
    print('hello, 执行函数test1')


print(test1())


def test2():
    print('hello, 执行函数test1')
    return

def test3(x, y):
    x2 = x ** 2
    y2 = y ** 2
    return x2, y2


result = test3(3, 4)
print(result, type(result))

r1, r2 = test3(3, 4)
print(r1, r2)