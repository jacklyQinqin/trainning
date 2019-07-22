#!/usr/bin/python3
# Filename:

import  os

#创造一个异常.zeroDiv异常.
def  except1():
    return  3.0/0
#创造一个正常.
def usual1():
    return  1

#版本1.简单版 精确拦截.
try:
    except1()
except(ZeroDivisionError):
    print("#Output 1: 除数为0")
#版本2  通配符.
try:
    except1()
except(SyntaxError):
    print("#Output 2:语法错误")
except:
    print("#Output 2:通配异常.反正就是exception中的异常")

#版本3: 加入else 如果没有异常.try正常执行, 则执行else else和try的执行结果有关..
try:
    usual1()
except(SyntaxError):
    print("#Output 3:语法错误")
except(KeyboardInterrupt):
    print("#Output 3:键盘输入错误")
except:
    print("#Output 3:拦截所有的exception中定义的异常")
else:
    print("#Output 3:不在以上异常,try执行正确")

#版本4:无论是否异常,都会最终执行到finally.用来清理.推荐使用此版本.
try:
    #usual1()
    except1()
except(SyntaxError):
    print("#Output 4:语法错误")
except(KeyboardInterrupt):
    print("#Output 4:键盘输入错误")
except:
    print("#Output 4:拦截所有的exception中定义的异常")
else:
    print("#Output 4:不在以上异常,try执行正确")
finally:
    print("#Output 4:结束try语句")


with open("a.txt") as f:
    print("打开成功")