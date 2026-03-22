import re
from functools import reduce

s1 = 'abc__2322ef'

# 匹配正确的用户名
print(re.match(r'^[a-zA-Z]\w{5,15}$', s1))
# 注意：{5, 15}里面不能有空格

# 匹配密码
s = 'xzq_2234w'
result = re.match(r'[a-zA-Z_][^!@#¥%^&*]{5,11}', s)
print(result)

# 匹配QQ号码
s = '10086111222'
# 5 - 11 位
result = re.match(r'[1-9]\d{4,10}$', s)
print(result)

# 检索所有的python源代码文件
s = '1.py 2.png ssx.csv qaq.txt xzq.py'
#文件名格式:  (数字字母_).py
result = re.findall(r'\b\w+\.py\b', s)
print(result)


# 验证输入的邮箱 163 126 qq 前面至少五位,至多11位
email = '738473800@qq.com'
result = re.match(r'\w{5,11}@(163|126|qq)\.(com|cn)$', email)
print(result)

phone = '010-12345678'
result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
print(result)  # <re.Match object; span=(0, 12), match='010-12345678'>
print(result.group())  # 010-12345678
print(result.group(1))  # 010
print(result.group(2))  # 12345678

# 爬虫
s = '<html>hello</h1>'
s2 = '<html>hello</html>'
result = re.match(r'<([0-9A-z]+)>(.+)</\1>$', s)
print(result)  # None
result = re.match(r'<([0-9A-z]+)>(.+)</\1>$', s2)
print(result)  # <re.Match object; span=(0, 18), match='<html>hello</html>'>
print(result.group(1))  # html
print(result.group(2))  # hello


# 分组取名
# 取名字 (?P<名字>正则) (?P=名字)
s = '<html>hello</h1>'
s2 = '<html>hello</html>'
result = re.match(r'<(?P<name1>\w+)>(.+)</(?P=name1)>$', s)
print(result)  # None
result = re.match(r'<(?P<name1>\w+)>(?P<msg>.+)</(?P=name1)>$', s2)
print(result)  # <re.Match object; span=(0, 18), match='<html>hello</html>'>
print(result.group('name1'))  # html
print(result.group('msg'))  # hello



# 提取数字并计算
s = '-3.14good87nice19bye'
nums = re.findall(r'-?\d+\.?\d*', s)
result = reduce(lambda x, item: x + float(item), nums, 0)
print(result)


# 匹配整数或者小数
s = '-3.14'
result = re.fullmatch(r'[+-]?(0|[1-9]\d*)(\.\d+)?', s)

print(result)

# \u4e00-\u9fa5 中文在国际编码中的范围
s = '1.py 2.png ssx.csv qaq.txt xzq.py 测试.py'
result = re.findall(r'[\u4e00-\u9fa5\w]+\.py\b', s)
print(result)