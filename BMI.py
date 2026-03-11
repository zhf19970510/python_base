# 计算一个人的BMI
h = float(input("请输入您的身高：（单位：米）\t"))
w = float(input("请输入您的体重（单位：千克）\t"))

# 开始计算
bmi = w / h ** 2
print(f"您的身高是：{h}米", end = '')
print(f"您的体重是：{w}千克", end = '')
print("你的BMI体质指数是：%.2f" % bmi, end = '\n')