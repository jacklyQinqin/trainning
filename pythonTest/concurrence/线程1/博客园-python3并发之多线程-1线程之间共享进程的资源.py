"""
全局变量在进程内被所有的线程共享.

"""
from threading import  Thread
from multiprocessing import  Process
import  os

def work():
    global  n
    n = 0

if __name__ == "__main__":
    #主进程中修改N的值,线程又给改为了0
    n = 100
    t1 = Thread(target=work)
    #t2 = Thread(target=work)
    t1.start()
    t1.join()
    print("n = ",n)

    n = 100
    p1 =Process(target=work)
    p1.start()
    p1.join()
    print("进程中的N为 ",n)