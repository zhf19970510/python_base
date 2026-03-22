"""
带参数的装饰器就是使用装饰器装饰函数的时候可以传入指定的参数：语法格式：@装饰器(参数,...)
    装饰器只能接收一个参数，并且只能是函数类型
    在装饰器外面包裹一个函数，让最外面的函数接收参数，返回的是装饰器
"""
import functools
import sys
import time
import os


def login(password_file):
    """
    定义了一个装饰器
    1. 文件如果存在，读取文件内容（用户信息）
    2. 文件不存在，创建一个文件，并且把用户信息录入到文件中
    :param password_file:   保存用户名和密码的文件，文件的格式：一行保存一个用户，{'username': '用户名', 'password': '密码'}

    :return:
    """

    def login_decorator(func):
        user_login_flag = False  # 用户还没有认证成功
        # 用户认证之前的准备工作
        users = []  # 存储所有的用户信息
        if os.path.exists(password_file):  # 文件存在，读取用户信息
            with open(password_file, 'r') as f:
                lines = f.readlines()
                for line in lines:  # 其中一行数据代表一个用户
                    user = eval(line)  # 把字符串当成字典
                    users.append(user)
        else:  # 文件不存在
            choice = input('是否要创建新用户（Y/N）：')
            if choice == 'Y' or choice == 'y':
                with open(password_file, 'w') as f:
                    username = input('请输入新的用户名：')
                    password = input('请输入新的密码：')
                    user = {'username': username, 'password': password}
                    users.append(user)
                    # 写入文件中
                    f.write(str(user) + "\n")
            else:
                print('没有用户信息，无法完成用户认证！只能退出')
                sys.exit(1)

        @functools.wraps(func)  # wraps 做一下伪装，是的对外访问无感，让调用者无感知，使用test1.__name__返回的还是test1
        def inner(*args, **kwargs):
            # 用户的认证
            nonlocal user_login_flag
            if not user_login_flag:  # 用户没有登录，现在开始马上登录
                un = input('请输入登录的用户名：')
                pwd = input('请输入登录的密码：')
                for u in users:
                    if un == u['username'] and pwd == u['password']:
                        print(f'登录成功，欢迎{un}登录')
                        user_login_flag = True
                        break
                else:   # 没有找到相同用户名和密码的用户
                    print('你输入的用户名或密码有误！')

            if user_login_flag:
                return func(args, kwargs)

        return inner
    return login_decorator


@login('users.txt')
def test1(*args, **kwargs):
    print('test1')
    time.sleep(1)


if __name__ == '__main__':
    test1()
    time.sleep(1)
    test1()
    test1()