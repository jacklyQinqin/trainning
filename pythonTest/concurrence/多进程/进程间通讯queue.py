'''
进程间通讯使用队列
父进程创建队列
并传递给子进程
相当于CC2640中的queue的使用。和全局状态指针的传递。
'''
from multiprocessing import Process ,Queue
import  os
import  time

def write(q):
    print("启动写子进程")
    while True:
        for chr in ['a','b','c','d','e']:
            q.put(chr)
        time.sleep(1)


def read(q):
    while True:
        chr = q.get()
        print('value = {0:s}'.format(chr))

if __name__=='__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()

