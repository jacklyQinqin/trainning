"""
多线程和多进程最大的不同在于多进程中,不能共享全局变量.全局变量只是一份原始数据的copy
进程间通讯可以通过queue.
线程中所有变量共享.所以各个线程间需要使用 lock.来防止数据的混乱.
最大的危险在于多个线程同时操作一个变量会导致数据紊乱.所以需要使用lock
"""

import threading
import time

num  = 0


def run(n):
    global  num #引用全局变量
    for i in range(5000000):
        num = num + n
        num = num - n
        #print(num)







if __name__ == "__main__":
    t1 = threading.Thread(target=run,args=(1,))
    t2 = threading.Thread(target=run,args=(6,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)
