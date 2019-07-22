"""

"""
import threading

import time

num  = 0

#创建一个全局的threadlocal对象.
#每个线程有独立的存储空间.
#每个线程对threadlocal对象都可以读写.但是互不影响.
#我靠这玩意儿不就是拷贝么.
#每个线程的local.x就是线程的局部变量.但是可以从全局变量引入数据
#比如 local.x = num.
#方便的是,使用一个local.可以为每一个线程添加一个local.x.
#作用.可以为每个线程绑定一个数据库连接,或者http请求,用户身份信息等.
#这样一个线程的所有调用到处理函数都可以方便的访问这些资源.而不用等待解锁.

#本地化的意思就是只要在一个函数中使用,那么在多线程调用这个函数的时候,每个线程都有一个独立的local数据.


local = threading.local()
lock1 = threading.Lock()

def run(n):
    global  num #引用全局变量
    print("执行开始{0:s}".format(str(time.time())))

    for i in range(5000000):
        #为了防止执行过程失败,导致返回.这里使用try.
        #finally.以防止死锁.
        with lock1:
            num = num + n
            num = num - n

    print("执行结束{0:s}".format(str(time.time())))

if __name__ == "__main__":
    t1 = threading.Thread(target=run,args=(1,))
    t2 = threading.Thread(target=run,args=(6,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)
