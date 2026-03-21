s1 = 'hello'
s2 = "hello"
s3 = """hello"""
s4 = '''hello'''
print(s1 == s2)
print(s4 == s3)
print(s1 == s4)
print(s2 == s3)

s5 = 'hello\nworld'
print(s5)

s6 = 'I\'m Tom'
print(s6)

s7 = '我是\"湖南\"人'
print(s7)

c1 = s1[1]
print(c1)

# 序列对象 [开始位置下标:结束位置下标:步长];口诀：包头不包尾

s = 'abcefghijk'
print(s[2:6:1])
print(s[2:6])
print(s[-8:-4])
# 从0下表截取，开始的0可以不写，默认下标从0位置开始
print(s[:4])
# 默认截取到最后一个下标，所以如果截取到最后一个位置，结束位置下标可以不用写
print(s[5:])
print(s[:])

# 字符串倒序
print(s[::-1])

# 字符串中的函数
"""
1. 字符串查询（inex, find）
建议使用find，因为如果没有找到匹配的字符串，index方法会报异常
find: 正向查找，没有找到返回-1
rfind: 从右到左开始查找
index: 类似于find，只不过没有找到会报异常
"""

ss = 'hellopythonworld'
print(ss.find('py'))
# print(ss.index('hi'))   # 这行输出会报错
print(ss.find('hi'))
print(ss.rfind('py'))

"""
2. 字符串大小写转换（upper，lower，swapcase，capitalize，title）
upper：将字符串中所有元素都转为大写
lower：将字符串中所有元素都转为小写
swapcase：交换大小写。大写转换为小写，小写转换为大写
capitalize：第一个大写，其余小写
title：每个单词的第一次字符大写，其余均为小写
"""

"""
3. 字符串对齐（center，just和zfill）
"""

"""
4. 分割字符串（split，splitlines和partition
"""

sss = 'I am a student'
print(sss.split(' '))   # 分割，分隔符不会在结果中出现
print(sss.partition(' '))   # 分区：分隔符单独一个区

"""
5. 合并与替换（join，replace）
join(seq): 以指定字符串作为分隔符，将seq中的所有元素合并为一个新的字符串
replace(old, new [,max]): 将字符串中的old替换为new，如果max指定，则替换不超过max次
"""
print(sss.replace('student', 'worker'))

"""
6. 判断字符串：
isIdentifier: 判断字符串是不是合法标识符（字符、数字、下划线）
isspace: 判断字符是否只有空白符（回车、换行和水平制表符）
isalpha: 判断字符串是否全部由字母组成
isdecimal: 判断字符是否全部由十进制的数字组成，不包括中文、罗马字符
isdigit: 判断字符串只包含数字，不包括中文数字
isnumeric: 判断字符串是否全部由数字组成，中文数字也算
isalnum: 判断字符串是否由字母和数字组成
islower: 判断字符串中的字符是否全部为小写，字符串至少有一个字符
isupper: 判断字符串中的字符是否全部为大写，字符串至少有一个字符
startwith(str): 检查字符串是否以str开头，若是则返回true
endwith(str): 检查字符串是否以str结尾, 若是则返回true
"""

"""
7. 去除两端多余字符操作(strip)
lstrip(str): 去掉左边的str字符（不是字符串），默认为空白字符
rstrip(str): 去掉右边的str字符
strip(str): 去掉左右两边的str字符
"""

print(sss)
# 获取字符串长度
print(len(sss))