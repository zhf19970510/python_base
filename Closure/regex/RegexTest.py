"""
re模块用来做正则表达式匹配

1. match函数
re.match 尝试从字符串的起始位置匹配一个模式，匹配成功则返回一个匹配对象（这个对象包含了匹配的信息），如果不是起始位置匹配成功的话，match() 返回的是空
注意：match只能匹配到一个

2. search函数
re.search 扫描整个字符串，匹配成功则返回一个匹配对象（这个对象包含了我们的匹配信息）；当然，若是找不到则返回None值。
注意：search也只能匹配到一个，找到符合规则的就返回，不会一直往后找

3. findall函数
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表；如果没有找到匹配的，则返回一个空列表
"""
import re

s = 'python123python567python999'

# match函数，只会从第一个字符开始匹配
result = re.match('python', s)

print(result)
print(result.group())
print(result.span())

# match函数，不只是从第一个开始匹配
result = re.match('python', s)

print(result)
print(result.group())
print(result.span())

# findall函数，查询多个子串
result = re.findall('python', s)
print(result)

# fullmatch, 全字符串匹配，相当于字符串比较相等
result2 = re.fullmatch('python', s)
print(result2)

# 匹配一个数字
print(re.search(r'\d', r'python893_\n abc'))
print(re.search(r'[0-9]', r'python893_\n abc'))

# 匹配单词字符
print(re.search(r'\w', r'python893_\n abc'))

# 匹配非单词字符
print(re.search(r'\W', r'python893_\n abc'))

# 匹配所有数字
print(re.search(r'\d+', r'python893_\n abc'))

# 找到所有的非空白字符
print(re.search(r'\S+', r'python893_\n abc'))

# 找到所有的单词字符
print(re.search(r'\w+', r'python893_\n abc'))


# 边界的元字符
tel1 = 'awhahlf@163.com，affafafafaaaaaaaaaaaaaaaa@163.com，abcefg@163.com afa_@163.com'
print(re.search(r'^[a-zA-Z]\w{5,17}@163.com', tel1))

print(re.findall(r'\b[a-zA-Z]\w{5,17}@163.com\b', tel1))


# ^ 还有取反的意思
s3 = '1231243243'
print(re.search(r'[^0-9]+', s3))


# 表示分组的元字符
ret = re.match(r"[1-9]?\d$|100","78")
print(ret.group())

# 当继续匹配100时 依旧使用 | 进行分支匹配，我们看是可以成功的，通过右方的表达式进行匹配结果
ret = re.match(r"[1-9]?\d$|100","100")
print(ret.group())

# 在括弧中加入了分支进行判断，根据结果判断，也匹配到结果，
ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret.group())

ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
print(ret.group())

ret = re.match(r"<(?P<my_name>[a-zA-Z]*)>\w*</(?P=my_name)>", "<html>hh</html>")


print(ret.group())
