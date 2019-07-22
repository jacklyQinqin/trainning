"""
典型:
比如银行卡的操作.
如果是两个线程,同时一个存钱,一个取钱.就出现问题.

线程锁确保了某一段代码只能由一个线程完整执行.

如果使用了多个锁.多个线程间持有不同的锁,导致有些线程死锁.此时需要操作线程的强行终止.
所以逻辑一定要清晰.


写法1.
lock.arquire()
try:
    pass
finally:
lock.release()

#with lock可以自动上锁与解锁.
写法2:
with lock:
    pass stement.





"""

import threading

import time

num  = 0
lock1 = threading.Lock()

def run(n):
    global  num #引用全局变量
    print("执行开始{0:s}".format(str(time.time())))

    for i in range(5000000):
        lock1.acquire()
        #为了防止执行过程失败,导致返回.这里使用try.
        #finally.以防止死锁.
        try:
            num = num + n
            num = num - n
        finally:
            lock1.release()
        #print(num)
    print("执行结束{0:s}".format(str(time.time())))

if __name__ == "__main__":
    t1 = threading.Thread(target=run,args=(1,))
    t2 = threading.Thread(target=run,args=(6,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)
