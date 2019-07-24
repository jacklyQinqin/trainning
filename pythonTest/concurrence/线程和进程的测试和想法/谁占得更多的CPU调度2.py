#_*_coding:utf-8_*_
#!/usr/bin/env python
"""
经过测试,进程和线程的性能上,
没有什么太大差别.

至少在进行 1 打印,
2,打印+等待0.1s.两种方式,通过四线程,和四进程的比较.性能相差不大.

"""
import random
import time
from multiprocessing import Process
from threading import Thread


class Piao(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        while 1:
            print('%s piaoing' %self.name)
            #time.sleep(0.1)
if __name__=="__main__":
    p1=Piao('aaa')
    p2=Piao('bbb')
    p3=Piao('ccc')
    p4=Piao('ddd')

    p1.start() #start会自动调用run
    p2.start()
    p3.start()
    p4.start()
    print('主线程')