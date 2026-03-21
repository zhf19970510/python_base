"""
字典相关操作和函数
len(dict): 返回字典dict对应的项数
d[k]: 返回键k相应的值
k in d: 检查键 k 是否包含于字典d

字典中的函数：
clear: 可以清除字典中的所有数据
fromkeys: 使用该方法可以创建一个新字典，其中包含指定的键，且每个键对应的值都是None
get: 直接访问字典中的值
items: 会返回一个包含所有字典项的列表，其中每个元素都为键值对的形式，且排列顺序不确定
keys: 返回字典中的所有key，组成一个列表
values: 返回字典中的所有value
pop: 删除并返回指定key的值
"""

# 创建字典
dict2 = {}  # 空字典
dict1 = {'name': 'laozeng', 'age': 34}
dict3 = dict([('name', 'zs'), ('age', 44)])
dict4 = dict(name='ls', age=53, city='beijing')
print(dict2)
print(dict1)
print(dict3)
print(dict4)

# 新增和修改
dict1['address'] = 'shanghai'
print(dict1)
dict1['age'] = 44
print(dict1)

# 删除
dict1.pop('age')
print(dict1)
del dict1['address']
print(dict1)
dict1.clear()
print(dict1)

# 查询
dict1 = {'name': 'laozeng', 'age': 34, 'address': 'shanghai'}
if 'address' in dict1:
    print(dict1['address'])

# 字典中的一些函数
new_dict = dict.fromkeys(['name', 'age'])
print(new_dict)
new_dict['name'] = 'wangwu'

print(dict1['address'])
print(dict1.get('address'))

# 字典的遍历
# items 把所有的项放到一个列表中
for k, v in dict1.items():
    print(k, v)
    print(f'key={k}, value={v}')

print('-' * 50)
for k in dict1.keys():
    print(f'key={k}, value={dict1[k]}')

print('-' * 50)
for v in dict1.values():
    print(v)