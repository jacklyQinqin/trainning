
from multiprocessing import  Process

from time import  sleep
#全局变量进程中不能共享
#定义的全局变量，在子进程中的修改，对主进程没有影响。
#在主进程中的修改对子进程也不会产生影响。
#子进程应当会给变量做一份拷贝。
#两者是完全不同的两个变量
#全局变量的作用范围只限于父进程。
#子进程用global引入，就相当于在子进程中重新应用了初始定义。！
#同样，父子进程和兄弟进程，都不能共享全局变量

num = 100
def run():
    print("子进程开始")
    global  num
    num+=1
    print("子进程中的num为{0}".format(num))
    sleep(0.2)
    print("子进程结束")

if __name__ =='__main__':
    print("父进程开始")
    num += 2
    print("父进程中的num为{0}".format(num))

    p = Process(target=run)
    p.start()
    p.join()
    print("父进程结束")
