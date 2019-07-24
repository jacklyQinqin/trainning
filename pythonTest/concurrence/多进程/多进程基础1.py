# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:55:47 2019

@author: Administrator
"""


#多进程必须导入的对象
'''
对于操作系统来说。一个任务就是一个进程。
进程是系统中程序执行和资源分配的基本单位。
每个进程都有自己的数据段，代码段和堆栈段。

'''
import sys
from multiprocessing import Process
from time import sleep


#版本1.无法多进程。 
# 子进程要执行的代码
#此版本无法实现多进程
def run_proc(name):
    while True:
        print('Run child process %s (%s)...' % (name, os.getpid()))
        sleep(1.2)

if __name__=='__main__':
    while True:
        print("Output1 : Process sub :{0:s}".format("1"))
        sleep(2)
    run_proc()