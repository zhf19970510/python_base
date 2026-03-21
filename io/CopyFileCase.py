import os

"""
案例：实现一个文件夹中（目录中可能还有子目录），拷贝所有的py文件到另一个指定的目录中

给定目录：D:\dir_test\py_base_test
拷贝的目标目录：D:\dir_test_target
"""


def copy_dir(source_dir, destination_dir):
    """
    拷贝source_dir目录中所有的.py文件到另一个destination_dir中
    :param source_dir:  原始目录
    :param destination_dir: 目标目录
    :return:    返回一共拷贝的文件数量
    """
    sum_count = 0
    for f in os.listdir(source_dir):  # 其中的f代表目录下的所有文件（目录）名
        # 把文件名和目录拼凑成一个完整的绝对路径
        f_path = os.path.join(source_dir, f)
        if os.path.isfile(f_path) and f.endswith('.py'):  # 表示f是一个普通文件，并且也是py文件
            # 拷贝该文件到指定目录中
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            # 拼凑一个拷贝之后的目标文件绝对路径
            sink_path = os.path.join(destination_dir, f)
            # 拷贝文件内容到sink_path中
            num = copy_file(f_path, sink_path)
            sum_count += num
        elif os.path.isdir(f_path):
            # 采用递归函数的写法
            # 为了保持同样的目录结构，目标目录要跟着变化
            new_destination_dir = os.path.join(destination_dir, f)
            copy_dir(f_path, new_destination_dir)
    return sum_count


def copy_file(source_file, sink_file):
    """
    拷贝单个文件，把source_file文件中的内容拷贝到sink_file中
    :param source_file: 源文件绝对路径
    :param sink_file:   目标文件绝对路径
    :return:    拷贝成功返回1
    """
    # 第一种，考虑到文件都是小文件，可以一次性读取全部文件内容，并一次性写入新文件
    with open(source_file, mode='r', encoding='utf-8') as source_f:
        content = source_f.read()
        with open(sink_file, mode='w', encoding='utf-8') as sink_f:
            sink_f.write(content)
    return 1


copy_dir(r'D:\dir_test\py_base_test', r'D:\dir_test_target')


# 第二种：考虑到文件都比较大，没办法一次性把整个文件读到内存中，每次从源文件中读取一部分内容，并且写入到新文件中，copy_file方法的替代版
def copy_file2(source_file, sink_file):
    source_f = open(source_file, mode='r', encoding='utf-8')
    sink_f = open(sink_file, mode='w', encoding='utf-8')
    while True:
        content = source_f.read(1024 * 10)  # 每次读取10KB
        if content == '' or  content is None:   # 没有读取到数据
            break   # 意味着文件读取完了
        sink_f.write(content)

    source_f.close()
    sink_f.close()
    return 1