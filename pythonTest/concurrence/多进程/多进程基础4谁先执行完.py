# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:11:24 2019

@author: Administrator
"""

from multiprocessing import Process
import os
from time import sleep
import sys
#版本4.1
#如果主进程先执行完呢？子进程会接着执行吗？
#实践证明。子进程仍然在执行。

#但是通用的方法。
#是父进程要等待子进程结束。再执行父进程的退出。
#通用的方法是父进程创建几个子进程来进行运算。
#父进程什么都不干。子进程都结束之后，执行父进程的退出即可
#采用的方法是 p.join()



# def run_proc1():
#     while True:
#        print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
#        sleep(1.1)
# def run_proc2():
#     while True:
#         print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
#         sleep(1.2)
# def run_proc3():
#     while True:
#         print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
#         sleep(1.3)
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
#     #while True:
#     if True:
#         print('主进程1的PID是：{0:s}'.format(str(os.getpid())))
#         sleep(2)
#     print('主进程结束')



#版本2.子进程先结束。
def run_proc1():
       print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
       sleep(1.1)
       print('子进程1结束')
def run_proc2():
        print('子进程2的PID是：{0:s}'.format(str(os.getpid())))
        print('子进程2结束')
def run_proc3():
        print('子进程3的PID是：{0:s}'.format(str(os.getpid())))
        sleep(1.3)
        print('子进程3结束')
if __name__=='__main__':
    print("主进程启动（主进程就是父进程）")
    #创建一个进程
    #参数1 进程对应的函数名。
    #参数2 传参
    p1 = Process(target=run_proc1,args=())
    p2 = Process(target=run_proc2,args=())
    p3 = Process(target=run_proc3,args=())
    p1.start()
    p2.start()
    p3.start()
    while True:
        print('主进程的PID是：{0:s}'.format(str(os.getpid())))
        sleep(2)
    print('主进程结束')