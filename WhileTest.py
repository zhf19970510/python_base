# 计算 1 ~ 100 的所有奇数和

n = 1
my_sum = 0
while n <= 100:
    if n & 1 != 0:
        my_sum += n
    n += 1

print("my_sum = %d" % my_sum)

# 输出 9 * 9 乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        # 把改行的所有算式输出
        print(f'{j} * {i} = {i * j}', end='\t')
        j += 1
    i += 1
    print()
print()