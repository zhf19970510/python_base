"""
在Python中，每个Python文件都可以看作一个模块，模块的名字就是文件的名字
所以：自定义模块名必须要符合标识符命名规则

注意：
1. 如果使用 from ... import ... 或 from ... import * 导入多个模块的时候，且模块内有同名功能。
当调用这个同名功能的时候，调用到的是后面导入的模块的功能

2. 当导入一个模块，Python解释器对模块位置的搜索顺序是：
a. 当前目录
b. 如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。sys.path可以查看

3. 自己的文件名不要和已有模块名重复，否则导致模块功能无法使用

4. __all__
如果一个模块文件中有该变量，当使用 from xxx import *导入时，只能导入这个列表的元素但是：import 模块名字 的方式，不起作用

G:\commonTool\python-3.12\Lib\site-packages 这个目录存储下载的第三方的包
"""
import sys

from my_module import *

print(my_sum(8))

print(test(6))

# from my_module2 import *
# # 调用到同名功能时，调用到的是最后面导入的模块的功能
# print(test(6))
# print(my_sum(8))

print('-' * 50)
from my_module2 import test as other_test
# 调用到同名功能时，调用到的是最后面导入的模块的功能
print(test(6))
print(my_sum(8))
print(other_test(6))

import sys
print('-' * 50)
print(sys.path)

from __all__module_test import *

testA()
testB()
# testC()   # 会报错，因为__all__中没有暴露该模块

from package.my_module import *

print(my_sum(5))