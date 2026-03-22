import time

# 当前系统时间的时间戳，（秒）
print(time.time())

# 易读格式的时间
print(time.ctime())

# ctime 还可以根据你指定的时间戳得到时间对象
print(time.ctime(1774053966))

# 时间元组
print(time.gmtime())
print(time.gmtime(1774053966).tm_year)

print('*' * 25 + '时间格式化' + '*' * 25)
# 时间格式化
print(time.strftime("%Y-%m-%d", time.gmtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y年%m月%d日 %H:%M:%S"))

# 把字符串转换为时间戳
print(time.strptime('2026-03-21 09:29:30', '%Y-%m-%d %H:%M:%S'))