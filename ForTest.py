# range函数，包头不包尾
my_sum = 0

for i in range(1, 100, 2):  # 最后一个参数表示步进长度，默认为1,
    my_sum += i
print(f'结果是: {my_sum}')

my_sum = 0
# 第二种写法
for i in range(100):
    if i & 1 != 0:
        my_sum += i
print(f'结果是: {my_sum}')

my_sum = 0
# 第三种写法
i = 0
while True:
    i += 1
    if i > 100:
        break
    if i & 1 != 0:
        my_sum += i
print(f'结果是: {my_sum}')

my_sum = 0
# 第三种写法
for i in range(100):
    if i & 1 == 0:
        continue
    my_sum += i
print(f'结果是: {my_sum}')

# 9 * 9 乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} x {i} = {i * j}', end='\t')
    print()
print()