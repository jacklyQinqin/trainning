"""
什么是PID
process id
所以,一个进程内的所有线程都共享一个pid.
就相当于一个车间内的所有流水线都在这个编号的车间内.

"""


from threading import  Thread
from multiprocessing import Process
import  os

def work():
    print('Output #1Hello,子线程的PID {0!s}'.format(os.getpid()))
def work2():
    print('Output #2 Hello,子进程的PID {0!s}'.format(os.getpid()))
if __name__ == "__main__":
    #part1 在主进程下开启多个线程.每个线程都和主进程的pid一样.
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    print('主进程的PID是', os.getpid())

    #part2 开启多个进程.每个进程都有不同的PID.
    p1 = Process(target=work2)
    p2 = Process(target=work2)
    p1.start()
    p2.start()
    print("主进程的PID是{0!s}".format(os.getpid()))


