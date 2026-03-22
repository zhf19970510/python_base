"""
datetime模块的五大类：
1. datetime.date: 表示日期的类，主要用于处理年、月、日
2. datetime.time: 表示时间的类，主要用于处理时、分、秒
3. datetime.datetime: 表示日期时间的类，date和time类的综合使用，可以处理年、月、日、时、分、秒；
4. datetime.timedelta: 表示时间间隔，即两个时间点的间隔，主要用于做时间加减的
5. datetime.tzinfo: 时区的相关信息
"""
from datetime import datetime, timedelta, date, time

print('-' * 25 + 'date对象基本使用' + '-' * 25)
# 创建date对象
d = date(2026, 3, 25)
print(d)

# 获取当前日期
d = date.today()
print(d)

# 得到date对象的时间元组
print(d.timetuple())

# 得到date对象的星期
print(d.weekday())

# 获取日期的年份，第几周，周几
print(d.isocalendar())
print(d.isocalendar().weekday)

# 格式化
print(d.strftime('%Y-%m-%d'))

print()
print('-' * 25 + 'date对象的替换' + '-' * 25)
print()

new_date = d.replace(month=10, day=1)
print(new_date)
print(d)

print()
print('-' * 25 + 'time对象基本使用' + '-' * 25)
print()

# 创建time对象
tm = time(hour=10, minute=20, second=30)
print(tm)
print(tm.hour, tm.minute, tm.second, tm.microsecond)

tm1 = tm.replace(hour=21, minute=30, second=40)
print(tm1)
print(tm1.strftime('%H:%M'))

# datetime对象操作
print()
print('-' * 25 + 'timetime对象基本使用' + '-' * 25)
print()

dt = datetime(2018, 8, 8, 17, 23, 34)
print(dt)
# 当前系统时间datetime
dt2 = datetime.now()
print(dt2)
# 得到datetime对象的时间元组
print(dt2.timetuple())
print(dt2.timetuple().tm_mon)
# 时间格式化与解析时间
print(dt2.strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.strptime('2026年3月21日 10时30分45秒', '%Y年%m月%d日 %H时%M分%S秒'))

# 得到国际标准的时区时间
# print(dt2.utcnow())

# 得到datetime的时间戳
print(dt2.timestamp())

print()
print('-' * 25 + 'timedelta对象基本使用' + '-' * 25)
print()

td = timedelta(days=2, hours=3)
print(td)

# 在现在的时间基础上，往后两天的时间
dt3 = datetime.now() + timedelta(days=2)
print(dt3)

# 得到当前时间的前两天
dt3 = datetime.now() - timedelta(days=2)
print(dt3)

dt3 = datetime.now() + timedelta(days=-2)
print(dt3)

ini_time_str = '2020/8/3 23:00:51'
end_time_str = '2020/9/1 7:48:50'
dt4 = datetime.strptime(ini_time_str, '%Y/%m/%d %H:%M:%S')
dt5 = datetime.strptime(end_time_str, '%Y/%m/%d %H:%M:%S')
td1 = dt5 - dt4
print(type(td1))
print(td1.days, td1.seconds, td1.microseconds)


print()
print('-' * 25 + '综合练习' + '-' * 25)
print()

print('1. 输入一个日期，计算这个日期是当年的第多少天')
# input_str = input('请输入一个日期:')
input_str = '2026-03-21'
d = datetime.strptime(input_str, '%Y-%m-%d')
# 方法一
days = d.strftime('%j')
print(f'{input_str}是{d.year}年中的第{days}天')

# 方法二
days = d.timetuple().tm_yday
print(f'{input_str}是{d.year}年中的第{days}天')


print('2. 求出上个月的最后一天')
# 方法一
dt8 = datetime.now().replace(day=1) - timedelta(days=1)
print(f'当前月的上一天是{dt8.strftime('%Y-%m-%d')}')

# 方法二
d1 = date.today()
result = date(year=d1.year, month=d1.month, day=1) - timedelta(days=1)
print(f'当前月的上一天是{result}')

