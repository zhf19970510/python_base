"""
set集合：
由一系列不重复的不可变类型变量组成的可变散列容器
相当于只有键没有值的字典（键则是集合的数据）

创建集合使用{} 或 set(), 但是如果要创建空集合只能使用set(), 因为{}用来创建空字典

特点：
1. 集合不能出现重复的数据，自动去掉重复数据
2. 集合数据是无序的，故不支持下标
"""

set2 = set()

set1 = {'abc', 100, 78, 3,14}
print(len(set1))

# 添加
set1.add(99)
set1.add('hello')
print(set1)

# 删除
set1.remove('hello')
print(set1)

# for 可以遍历
for i in set1:
    print(i)

# 元组不可放入不可变类型
set3 = {'hello', (100, 200)}
print(set3)
# set4 = {'hello', (100, 200), [300, 400]}    # TypeError: unhashable type: 'list'
# print(set4)