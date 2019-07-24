# from multiprocessing import Process
# import os
# from time import sleep
#
# #版本8.1.多个子进程分别创建添加。
# def run_proc1():
#        print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
#        sleep(1.1)
#        print('子进程1结束')
# def run_proc2():
#         print('子进程2的PID是：{0:s}'.format(str(os.getpid())))
#         sleep(1.2)
#         print('子进程2结束')
# def run_proc3():
#         print('子进程3的PID是：{0:s}'.format(str(os.getpid())))
#         sleep(1.3)
#         print('子进程3结束')
# if __name__=='__main__':
#     print("主进程启动（主进程就是父进程）")
#     #创建一个进程
#     #参数1 进程对应的函数名。
#     #参数2 传参
#     p1 = Process(target=run_proc1,args=())
#     p2 = Process(target=run_proc2,args=())
#     p3 = Process(target=run_proc3,args=())
#     p1.start()
#     p2.start()
#     p3.start()
#     print('主进程的PID是：{0:s}'.format(str(os.getpid())))
#     sleep(2)
#     print('主进程结束')


import os
import time
from multiprocessing import Pool


#版本8.2 多个子进程使用 pool来管理。
def run_proc1():
       print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
       print('子进程1的开始时间为{0}'.format(time.time()))
       time.sleep(1)
       print('子进程1结束')
def run_proc2():
        print('子进程2的PID是：{0:s}'.format(str(os.getpid())))
        time.sleep(1.5)
        print('子进程2结束')
def run_proc3():
        print('子进程3的PID是：{0:s}'.format(str(os.getpid())))
        time.sleep(1.8)
        print('子进程3结束')
if __name__=='__main__':
    print("主进程启动（主进程就是父进程）")
    #创建一个进程
    #参数1 进程数量
    pp = Pool()
        #创建进程。放入进程池。
        #方便统一管理
    pp.apply_async(run_proc1, args=())
    pp.apply_async(run_proc2, args=())
    pp.apply_async(run_proc3, args=())
    #在调用join之前必须先关闭进程池
    pp.close()
    #在调用close之后。不能再往进程池放进程。
    #进程池调用join,会等待进程池所有子进程结束后在去执行父进程。
    pp.join()

    print('主进程的PID是：{0:s}'.format(str(os.getpid())))
    time.sleep(2)
    print('主进程结束')