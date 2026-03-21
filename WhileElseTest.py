import random

"""
循环可以和else配合使用, else下方缩进的代码指的是：当循环正常结束之后要执行的代码。
如果是break终止循环的情况，else下方缩进的代码将不执行
"""

print("-" * 50)
print("欢迎来到 鸿发 的《猜数游戏》")
print("规则一：系统每次会自动生成一个1~10之间的随机数")
print("规则二：每次游戏最多只能猜三次")
print("规则三：进入游戏或者继续玩：输入：yes或者y")
print("规则四：离开游戏，输入no或者n")
print("-" * 50)

# 定义一个记录游戏次数变量
n = 0
while True:
    order = input('请输入是否开始游戏：')
    if order == 'yes' or order == 'y':  # 用户想玩游戏
        number = random.randint(1, 10)  # 生成一个随机数
        n += 1
        print(f'正式开始第{n}次游戏')
        for i in range(1, 4):   # 用户最多可以猜三次
            my_num = int(input('请玩家输入所猜的数字'))
            if my_num == number:
                print(f'恭喜你猜中了，答案就是{my_num}')
                break
            elif my_num > number:
                print(f'你猜的数字太大了，还剩下{3 - i}')
            else:
                print(f'你猜的数字太小了，还剩下{3 - i}')
        else:   # 三次都猜错了
            print(f'你三次都错了，正确的答案是{number}')
    elif order == 'no' or order == 'n':     # 用户不想玩
        print('谢谢！GAME OVER')
        break
    else:
        print('请输入正确的指令')

