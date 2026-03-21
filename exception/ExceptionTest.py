
import traceback
f = None
try:
    f = open('abc.txt')
    s = f.readline()
    num = int(s.strip())
    print(num)
except FileNotFoundError:
    print(traceback.format_exc())
    print('文件不存在')
except ValueError:
    print(traceback.format_exc())
    print('值不对，不能转换')
except Exception:    # Exception 是所有异常的父类
    print(traceback.format_exc())
else:   # 没有异常会执行
    print('没有异常，高兴')
finally:    # 无论有无异常都会执行
    if f:
        print('不管有没有异常都会执行的代码')
        f.close()
print('程序完成')