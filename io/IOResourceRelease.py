"""
关闭（释放）资源
打开文件，写完内容之后，一定要关闭该文件，如果不关闭，极端情况下，会出现 Too many open files的错误
因为系统允许你打开的最大文件数量是有限的
"""

# 使用with语句自动释放资源
with open('./test5.txt', mode='w+', encoding='utf-8') as f:
    for i in range(10):
        f.write('hello\n')


