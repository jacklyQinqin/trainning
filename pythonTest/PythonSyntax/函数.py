import os
import sys
import time


def nowTime():
    return  time.time()

def currentPath():
    print("Output #1: Hello.jacklyQin")


print(nowTime())
currentPath()


#在 python 中，类型属于对象，变量是没有类型的：

a=[1,2,3]

a="Runoob"
#以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），
# 可以是指向 List 类型对象，也可以是指向 String 类型对象。