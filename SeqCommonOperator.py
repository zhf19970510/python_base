"""
一、数学运算符
（1）+: 用于拼接两个序列
（2）+=: 用原序列与右侧序列拼接，并重新绑定变量
（3）*: 重复生成序列中的元素
（5）< <= > >= == !=: 依次比较两个序列中元素，一旦不同则返回比较结果
"""

print('-' * 50)
print('数学运算符')

s1 = 'abc' + 'efg'
lst = [100]
lst2 = lst + [1, 3.14, 'abc']
lst += [1, 3.14, 'abc']
print(lst2)
print(lst)

print('-' * 50)
print([1, 2] * 50)
lst *= 50

lst1 = ['abc', 1, 2]
lst2 = ['abc', 2, 3]
print(lst1 > lst2)
print(lst1 < lst2)
print(lst1 <= lst2)

"""
二、成员判断：
数据 in 序列
数据 not in 序列
"""

print('-' * 50)
print('成员判断')

t1 = (100, 200)
print(10 in t1)
print(100 in t1)
print(10 not in t1)

"""
三、下标和切片
"""

print('-' * 50)
print('下标和切片')

lst = [12, 'ab', 12, '3.14', [1, 2]]
print(lst[1])
print(lst.index(12))
print(lst[1:3])

"""
四、Python内置函数操作
（1）len(x) 返回序列的长度
（2）max(x) 返回序列的最大值元素
（3）min(x)返回序列的最小值元素
（4）sum(x) 返回序列中所有元素的和（元素必须是数值类型）
"""

print('-' * 50)
print('内置函数')

t1 = (100, 200)
print(max(t1))
print(min(t1))
print(sum(t1))

print(max('hello'))