# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:11:24 2019

@author: Administrator
"""

import os
import sys
from multiprocessing import Process
from time import sleep


#版本6.1如果有个进程是没有等待
#测试结果是只执行子进程1.其他没有执行，估计是因为优先级的问题
#高优先级的任务无法被打断
def run_proc1():
    while True:
        print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
        #sleep(1.1)
def run_proc2():
    while True:
        print('子进程2的PID是：{0:s}'.format(str(os.getpid())))
        sleep(1.2)
def run_proc3():
    while True:
        print('子进程3的PID是：{0:s}'.format(str(os.getpid())))
        sleep(1.3)

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
    p1.join()
    p2.join()
    p3.join()
    print('主进程结束')



#版本6.2如果有个进程是获取输入。q
#测试结果是其他两个子进程可以运行
#高优先级的任务无法被打断
def run_proc1():
        print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
        a =  input()
def run_proc2():
    while True:
        print('子进程2的PID是：{0:s}'.format(str(os.getpid())))
        sleep(1.2)
def run_proc3():
    while True:
        print('子进程3的PID是：{0:s}'.format(str(os.getpid())))
        sleep(1.3)

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
    p1.join()
    p2.join()
    p3.join()
    print('主进程结束')
