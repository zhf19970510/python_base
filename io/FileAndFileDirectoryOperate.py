"""
文件和文件夹的操作
在Python中文件和文件夹的操作要借助os模块里面的相关功能。OS模块是Python标准库中的一个用于访问操作系统功能的模块

"""
import os
"""
os.name                         # 查看当前操作系统的名字，"nt"表示windows，"posix" 表示linux
os.sep                          # 获取当前系统平台路径分隔符
os.getcwd()                     # 获取当前工作目录
os.environ[key]/os.getenv(key)  # 获取当前环境变量值
os.listdir(path)                # 列出指定目录path的所有文件和目录名
os.chdir(path)                  # 切换目录
os.mkdir(path)/os.mkdirs(path)  # 创建单层目录/多层目录
os.rmdir(path)/os.removedirs(path)  # 删除单层空目录/多层空目录
os.remove(file_name)            # 删除文件
os.rename(file_name, new_file_name) # 修改文件或目录名称
os.path.abspath(path)           # 获取指定相对路径的绝对路径
os.path.split(path)             # 获取指定路径的目录名和文件名
os.path.isfile(path)            # 判断指定路径目标是否为文件
os.path.isdir(path)             # 判断指定路径目标是否为目录
os.path.exists(path)            # 判断指定路径是否存在
os.path.splitext(path)          # 分离文件拓展名
os.path.join(path,*paths)       # 路径连接
os.path.base(path)              # 提取文件名
os.path.dirname(path)           # 提取文件路径
os.path.getsize(path)           # 返回文件大小
"""

print(os.getcwd())
dirList = os.listdir(r'D:\dir_test')  # r: 将指定路径作为原字符看待，不转义
print(dirList)
print(os.path.abspath('./test5.txt'))
print(os.path.split(r'G:\code\python_base\io\test5.txt'))

print(os.path.splitext(r'G:\code\python_base\io\test5.txt'))