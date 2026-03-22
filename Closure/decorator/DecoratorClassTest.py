class Login(object):
    def __init__(self, func):
        self.func = func

    # 如果是装饰器类，必须重写 __call__函数
    def __call__(self, *args, **kwargs):
        print('检查是否登录了，如果没有，则登录')
        return self.func(*args, **kwargs)

@Login
def comment():
    print('发布评论')


if __name__ == '__main__':
    comment()