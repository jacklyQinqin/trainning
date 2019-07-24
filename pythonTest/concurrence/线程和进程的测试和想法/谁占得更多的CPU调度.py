#_*_coding:utf-8_*_
#!/usr/bin/env python

import random
import time
from multiprocessing import Process


class Piao(Process):
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