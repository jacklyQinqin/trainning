# -*- coding: utf-8 -*-

#!/usr/bin/python3
"""
有效的处理异常和错误是程序健壮性的重要方面.
比如:你写的程序已经隐式的固定了需要处理的数据的类型等信息.如果其他的数据被传递进来,不符合你的预期,那么会将抛出一个异常.
永远不要假定你的用户会正确的操作,或者传递正确的数据.
永远要处理异常的情况.
异常情况的处理,会是程序健壮性的最大障碍.


是什么?有什么特性?怎么用?用在哪里?常用的方法是啥?
python包含集中built-in exception.
    1.IOError
    2.IndexError
    3.KeyError
    4.NameError  NameError: name 'my_list2' is not defined 引用了一个不存在的对象.
    5.SyntaxError
    6.TypeError
    7.UnicodeError
    8.ValueError
    9.ZeroDivisionError 除数0错误.

处理异常的方法:
    try  exception try后的模块是想执行的模块. exception 用来捕获异常.


    推荐使用:
    try exception else finally.
    try:
        想要执行的block
    exception xxError as detail:
        捕获某种异常
    else:
        如果执行成功,执行到这里.
    finally:
        最后都要执行这里,表示结束.

"""




# Calculate the mean of a sequence of numeric values
def getMean(numericValues):
    return sum(numericValues)/len(numericValues)
my_list2 = [32,"asf"]

"""
# Short version
try:
    print("Output #138: {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("Output #138 (Error): {}".format(float('nan')))
    print("Output #138 (Error): {}".format(detail))
"""



# Long version 推荐使用此种方法.
try:
    result = getMean(my_list2)
except TypeError   as detail: #可以分别捕获多个异常
    print ("Output #142 (Error): " + str(float('nan')))
    print ("Output #142 (Error):", detail)
except ZeroDivisionError   as detail: #可以分别捕获多个异常.
    print ("Output #142 (Error): " + str(float('nan')))
    print ("Output #142 (Error):", detail)
except SyntaxError   as detail: #可以分别捕获多个异常.
    print ("Output #142 (Error): " + str(float('nan')))
    print ("Output #142 (Error):", detail)
else:
    print ("Output #142 (The mean is):",result)
finally:
    print ("Output #142 (Finally): The finally block is executed every time")