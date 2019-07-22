"""
如果我们要确保balance计算正确，就要给change_it()上一把锁，
当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，
获得该锁以后才能改。由于锁只有一个，无论多少线程，
同一时刻最多只有一个线程持有该锁，
所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：

"""

#版本2加入线程锁
#当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，
#其他线程就继续等待直到获得锁为止。


import threading
import time
import  os
balance  = 0
lock = threading.Lock()

def change_it(n):
    global  balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i  in range(1000000):
        #先获取锁.才能继续执行
        lock.acquire()
        try:
            change_it(n)
        finally:
            #执行完毕,必须释放锁
            lock.release()


t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Output #2: balance的值为 {0!s}".format(balance))
print("{0}".format(os.cpu_count()))


