import  threading
import  time

import  support1

def aaa():
    for n in range(10000):
        for i in range(100000):
            n += i
    print(n)



#使用普通模式,耗时 48.45357608795166
"""
time1 = time.time()
aaa()
time2 = time.time()
print(time2-time1)
"""
#
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" \n")
#

#
# def printstr(str):
#     print(str)
#
#
# printstr(str="teee")
#
# def printinfo(arg1,* args2):
#     printstr(arg1)
#     print(args2)
#
#
# printinfo(1,1,2,3,4)
#
# a = 10
# def test():
#     #global  a
#     a = a + 1
#     print(a)
# test()


support1.print_func('jackqin')
support1.print_func('jackqin2')