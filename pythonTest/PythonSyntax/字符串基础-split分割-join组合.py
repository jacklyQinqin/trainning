# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:05:49 2019

@author: Administrator
"""

#split可以有两个参数。
#第一个参数是 单个或多个字符。表示什么时候执行分割操作
#第二个参数是数字，表示分割的次数
#默认情况下，如果没有这两个参数，则执行 空格 分割。不限次数。
#分割后形成一个list（列表）列表可以用负数操作。
string1 = "My deliverable is due in may"
string1_list1 = string1.split() #默认分割
string1_list2 = string1.split(' ',2) #空格分割2次，形成3个list元素
print("Output #21: {0}".format(string1_list1))
print("Output #22: {0}".format(string1_list2))
print("Output #22: \nFIRST PIECE:{0} \nSECONDE PIECE:{1} \nTHIRD PIECE:{2}"\
.format(string1_list2[0],string1_list2[1],string1_list2[2]))  
string2 = "Your,deliverable,is,due,in,june."
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1],string2_list[5],string2_list[-1]))

      
#join.将单个字符串连成一个长的字符串。
#join有一个参数，可以设置为单个或多个字符，这个参数在每个粘结在一起的元素之间。
#最后一个元素没有此参数。
#
print("Output #23: {0}".format(string2_list))
print("Output #25: {0}".format(','.join(string2_list)))
print("Output #25: {0}".format('####'.join(string2_list)))
#输出结果为:Your####deliverable####is####due####in####june.
