
# 描述一台汽车

class Car():

    # self代表当前实例对象本身
    def __init__(self, brand, type_name, category):
        print('开始初始化Car对象')
        # brand, type_name, category 都是对象属性（成员属性）
        # 汽车的品牌
        self.brand = brand
        # 汽车的型号
        self.type_name = type_name
        # 汽车的类型：SUV，轿车
        self.category = category

    def __new__(cls, *args, **kwargs):
        print('创建Car的对象')
        return super(Car, cls).__new__(cls)


    def run(self):          # 对象函数（成员函数）
        print('开起来')

c1 = Car('比亚迪', '汉', '中型轿车')
c2 = Car('一汽大众', '迈腾', '中型轿车')
c1.run()
c2.run()


"""
访问对象的属性和函数
1. 类外面访问：
    对象名.属性名字
    对象名.函数名字
    
2. 类里面访问
    self.属性名字
    self.函数名字
"""