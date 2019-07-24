
"""
Since Windows has no fork, the multiprocessing module starts a new Python process and imports the calling module.
If Process() gets called upon import, then this sets off an infinite succession of new processes (or until your machine runs out of resources).
This is the reason for hiding calls to Process() inside

if __name__ == "__main__"
since statements inside this if-statement will not get called upon import.
由于Windows没有fork，多处理模块启动一个新的Python进程并导入调用模块。
如果在导入时调用Process（），那么这将启动无限继承的新进程（或直到机器耗尽资源）。
这是隐藏对Process（）内部调用的原，使用if __name__ == “__main __”，这个if语句中的语句将不会在导入时被调用。

"""
"""
import  multiprocessing
import  threading

import  os
import  time

def work():
    print("this is work")
    time.sleep(2)
if __name__=="__main__":
    p1 = multiprocessing.Process(target=work)
    #p1.daemon = True
    p1.run()
   # p1.join()
"""




import random
import time
from multiprocessing import Process


class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s piaoing' %self.name)

        time.sleep(random.randrange(1,5))
        print('%s piao end' %self.name)
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