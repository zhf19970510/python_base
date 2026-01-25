from decimal import Decimal

my_name = '张三'
my_age = 18

print('my name is %s' % my_name)
print('my age is %s' % my_age)

print('myname is %s, my age is %s' % (my_name, my_age))
print('myname is %s, my age is %d' % (my_name, my_age))

# 特殊格式
money = 8923
num = 1.71

print('我的金额是:%5d' % money)

# 精确到小数点后1位 四舍五入
print('%.1f' % num)

num02 = 22.345
# 因为计算机只认识和处理二进制的数值，在实际的计算中，所有的数据都必须为二进制，计算后又转换回来，就是在这个过程中造成数据的截断误差
# 精确到小数点后2位 四舍五入，正确是22.35
print('%.2f' % num02)
print(Decimal(str(num02)).quantize(Decimal('0.00'), 'ROUND_HALF_UP'))