import threading
import time

def thead1():
    print("子线程名字为{0:s}".format(threading.current_thread().name))
    time.sleep(1)
    print("{0:s}线程程结束".format(threading.current_thread().name))

if  __name__ == '__main__':
    #任何进程默认启动一个线程。称为主线程。
    #主线程可以启动新的子线程。
    #和父进程与子进程的原理雷同。
    #current_theaad().返回当前线程的实例.

    print('主线程启动')
    print("主线程名字为:{0:s}".format(threading.current_thread().name))

    #创建子线程
    thread1 = threading.Thread(target=thead1 )
    thread2 = threading.Thread(target=thead1)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('主线程结束')