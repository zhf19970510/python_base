"""
Process类说明：
Process([group [,target [,name [,args [,kwargs]]]]])
group: 指定进程组，目前只能使用None
target: 执行的目标人物名
name: 进程名字
args: 以元组方式给执行任务传参
kwargs: 以字典方式给执行任务传参

Process创建的实例对象的常用方法：
start(): 启动子进程实例（创建子进程）
join(): 阻塞当前进程，等待子进程执行结束
terminate(): 不管任务是否完成，立即终止子进程

Process对象其他的函数与属性：
name: 进程的名字
daemon: 布尔值，是否是守护进程
pid: 进程ID
exitcode: 进程退出码
run(): 表示进程所要做的事情，通过向参数target指定一个函数的方式指定run的行为，或者在子类重载该方法
is_alive(): 判断进程是否还活着
"""
import time
from multiprocessing import Process


# 创建进程执行多任务

# 吃饭任务
def eat():
    for i in range(6):
        print('正在吃饭')
        time.sleep(0.3)

# 做作业任务
def work():
    for i in range(6):
        print('正在做作业')
        time.sleep(0.3)


if __name__ == '__main__':
    # 创建一个子进程，每个任务由一个独立的子进程来完成
    p1 = Process(target=eat, name='进程1')
    p2 = Process(target=work, name='进程2')

    p1.start()
    p2.start()

    # 主进程自动等待，所有的子进程去执行各自的任务。一直到所有的子任务都结束，主进程才结束
    