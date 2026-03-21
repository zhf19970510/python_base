"""
当函数内部出现局部变量和全局变量相同名字时，函数内部中的 变量名 = 数据,
此时理解为定义了一个局部变量，而不是修改全局变量的值，如果要修改全局变量，必须使用global
"""
a = 20
def test1():
    b = 100
    return b ** (1 / 2), a ** 2


print(test1())

print('-' * 50)

def test2():
    global a
    a = 30
    print(a)
    a = 40
    print(a)


test2()
print(a)

def test3(a, lst1 = [1, 2]):
    # 把a加入到列表中
    if a not in lst1:
        lst1.append(a)
    return lst1


print(test3(10))
print(test3(20))
print(test3(30, lst1=[60, 70]))
print(test3(40))