"""
IO流

打开文件流
文件对象 = open(目标文件, 访问模式)

读操作
    文件对象.read(): 默认读取整个文件。或者可以读取指定大小的数据
    文件对象.readlines()
    文件对象.readline()

写操作
    文件对象.write()

seek()指针操作
    seek(偏移量, 起始位置): 起始位置为: 0: 起始位置, 1: 当前位置, 2: 文件结尾位置
    tell() 函数返回当前指针位置。
关闭
    close()

访问模式：
"""

# 创建文件流
f = open('./test.txt', mode='r', encoding='utf-8')

print(f.read(10))

print('-' * 50)

f.seek(0)

print(f.read())

f.close()

#
print('-' * 50)
f1 = open('./test1.txt', mode='r', encoding='utf-8')
print(f1.readline())
print(f1.readline())
print(f1.readline())
print(f1.readline())
f1.close()

print('-' * 50)
f2 = open('./test2.txt', mode='r', encoding='utf-8')
print(f2.readlines())
f2.close()

# 写操作
print('-' * 50)
wf = open('test3.txt', mode='w', encoding='utf-8')

# 往文件中写入3个hello
# wf.write('hello\n' * 3)
for i in range(3):
    print(f'当前指针的位置：{wf.tell()}')
    wf.write('hello\n')

wf.close()

# 指针的移动操作
# 需求：在第一个hello的后面添加一个：world
"""
test4.txt原始文件内容：
hello
pythonjava
c++python
fastapi-django
"""
print('-' * 50)
wf = open('./test4.txt', mode='r+', encoding='utf-8')   # 既能读，又能写，不使用 w 或者 w+，是因为它们会对原有内容删除
# 但是直接使用r+也有问题，它在指定位置写入数据时，会造成覆盖
# 把指针移到第一个hello后面
wf.seek(5, 0)   # hello占用5个字符
# 把第一个hello后面的内容读取出来
after = wf.read()   # 读完之后，指针又到了文件末尾
wf.seek(5, 0)   # hello占用5个字符
wf.write('world' + after)
wf.close()