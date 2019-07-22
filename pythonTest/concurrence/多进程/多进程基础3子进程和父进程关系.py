# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:11:24 2019

@author: Administrator
"""

from multiprocessing import Process
import os
from time import sleep
import sys
#版本3.
#注意事项：在交互模式下，不能进入子进程。也就是在kernel的情况下。子进程不能执行
#如果是用spyder。需要在run的时候配置为 external system termial.

#如果父进程已经结束了呢？子进程还能继续执行吗？

def run_proc1():
    while True:
       print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
       sleep(1.1)
def run_proc2():
    while True:
        print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
        sleep(1.2)
def run_proc3():
    while True:
        print('子进程1的PID是：{0:s}'.format(str(os.getpid())))
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
    while True:
        print('主进程1的PID是：{0:s}'.format(str(os.getpid())))
        sleep(2)
