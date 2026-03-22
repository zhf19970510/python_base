"""
就是给已有函数增加额外功能的函数，它的本质就是一个闭包函数

装饰器的功能特点：
1. 不修改已有函数的源代码
2. 不修改已有函数的调用方式
3. 给已有函数增加额外的功能


#装饰器基本雏形：
def decorator(fn):  # fn 是目标函数
    def inner():
        '''执行函数之前
        fn()    # 执行被装饰的函数
        '''执行函数之后'''

"""

# 为了给comment()函数增加一个额外功能，定义一个装饰器
def login(func):    # 装饰器  参数必须是一个函数
    print('装饰器开始执行')

    def inner():
        print('检查是否登录了，如果没有，则登录')
        func()

    return inner

# 需要先登录，才能发布评论
@login
def comment():
    print('发布评论')

# 除了这种写法，还可以使用注解的方式完成装饰器功能
# comment = login(comment)
comment()