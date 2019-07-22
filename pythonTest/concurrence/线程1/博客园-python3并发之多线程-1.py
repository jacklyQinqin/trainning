

#开启线程的两种方式.方式1

import threading

import  time
def sayhi(name):
    time.sleep(2)
    print("hi,{0!s}".format(name))


if __name__ == '__main__':
    t = threading.Thread(target=sayhi,args=("jack",))
    t.start()
    print("主线程")

    