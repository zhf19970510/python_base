lst = []
lst = [12, 'ab', 12, '3.14', [1, 2]]

# 列表操作
"""
1. 下标和切片：查找、修改、截取
index: 返回指定数据所在位置的下标
count: 返回指定数据在当前列表中出现的次数
len函数(内置）: 访问列表长度，即列表中数据的个数
append: 列表结尾追加数据
extend: 列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
insert: 指定位置新增数据
pop: 删除指定下标的数据（默认为最后一个），并返回该数据
del（内置）: 删除
remove: 移除列表中某个数据的第一个匹配项
reverse: 逆序
sort: 重新排序
for循环遍历 
"""

# 查找
print(lst.index(12))
print(lst.count(12))
print(len(lst))

# 添加数据的操作
lst.append('hello')
print(lst)
lst.append(5)
print(lst)
lst.extend('world')
print(lst)
lst.extend(['a', 'b', 'c'])
print(lst)
# lst.extend(5)   # 会报错，extend添加的元素必须是序列
# print(lst)
lst.insert(0, 100)
print(lst)
lst.insert(4, 'world')
print(lst)

print('-' * 50)
lst.pop()
print(lst)
print(lst.pop(2))
print(lst)
del lst[2]
print(lst)
lst.remove('world')
print(lst)

# 对字符串逆序
print(lst[::-1])
lst.reverse()
print(lst)

lst2 = [4, 9, 98, 32, 2, 12]
lst2.sort()
print(lst2)
lst2.sort(reverse=True)
print(lst2)

for item in lst2:
    print(item)