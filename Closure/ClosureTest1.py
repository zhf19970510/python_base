"""
闭包形成的条件：
1. 在函数（函数里面再定义函数）嵌套的前提下，
2. 内部函数使用了外部函数的变量（还包括外部函数的参数）
3. 外部函数返回了内部函数

4. 比 ClosureTest 多了
"""

def say_hello(name, i):

    i = i * 2

    # 定义内部函数
    def say(msg, j):
        nonlocal name               # 告诉解释器，name是外部函数的变量
        name = '李四'                 # 在内部函数中，定义了一个局部变量而已
        print(f'对着{name}说{msg}')
        print(f'计算结果为{i * j}')

    print(name)
    say('你好', 3)
    print(name)
    return say

# f对象就是闭包
f = say_hello('张三', 2)
f('你好', 3)