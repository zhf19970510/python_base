"""
Python模块（Module），是一个Python文件，以.py结尾，模块能定义函数，类和变量，模块也能包含可执行代码

导入模块的5种方式：
1. import模块名
2. from 模块名 import 函数名
3. from 模块名 import *
4. import 模块名 as 别名
5. from 模块名 import 函数名 as 别名
"""
import random

# 第一种
# 模块
# import math
#
# # 模块名.函数(对象)
# print(math.log2(8))
# print(math.log(8, 2))

# 第二种：from 模块名 import *
# from math import *
#
# print(log2(8))
# print(log(8, 2))

# 第三种：from 模块名 import 函数名       # 精确导入
# from math import log2, log10

# print(log2(8))
# print(log10(100))

# 第四种
import multiprocessing as mp

# 第五种
from math import log2 as lg2


