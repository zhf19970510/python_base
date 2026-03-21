
class PasswordTooShortError(Exception):
    """
    自定义异常，密码太短了
    """
    def __init__(self, len, min_len):
        self.len = len
        self.min_len = min_len

    # 打印异常对象，就会打印str函数的返回值
    def __str__(self):
        print(f'你输入的密码长度是{self.len} 不能小于 {self.min_len} 字符长度')


def input_password():
    pwd = input('请输入您的密码')
    # 规定密码长度不能小于6个字符
    if(len(pwd) < 6):
        raise PasswordTooShortError(len(pwd), 6)



if __name__ == '__main__':
    try:
        input_password()
    except Exception as err:
        print(err)