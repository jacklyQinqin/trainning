# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:11:24 2019

@author: Administrator
"""

from multiprocessing import Process
#import sys
from time import sleep

#版本2.多进程 
# 子进程要执行的代码
#注意事项：在交互模式下，不能进入子进程。也就是在kernel的情况下。子进程不能执行
#如果是用spyder。需要在run的时候配置为 external system termial.
#
def run_proc1():
    while True:
       # print('Run child process %s (%s)...' % (name, os.getpid()))
       print("子进程1执行") 
       sleep(1.1)
def run_proc2():
    while True:
       # print('Run child process %s (%s)...' % (name, os.getpid()))
       print("子进程2执行") 
       sleep(1.2)
def run_proc3():
    while True:
       # print('Run child process %s (%s)...' % (name, os.getpid()))
       print("子进程3执行") 
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
        print("Output1 : Process sub :{0:s}".format("1"))
        sleep(2)
