
class Employ(object):
    """员工类"""

    # is_leave=0    表示在职    1 表示离职
    def __init__(self, name, gender, age, mobile_number, is_leave=0):
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile_number = mobile_number
        self.is_leave = False if is_leave == 0 else True


    def __str__(self):
        return f'{self.name}\t{self.age}\t{self.gender}\t{self.mobile_number}\t{"离职" if self.is_leave else "在职"}'


if __name__ == '__main__':
    e = Employ('张三', '女', 23, '123456')
    print(e.__dict__)   # 把python对象转换为字典
    print(vars(e))  # 也可以将python对象转换为字典
    print(e)