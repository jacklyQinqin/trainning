# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:51:34 2019

@author: Administrator
"""

#字符串基础内置操作
# str1 + str2  字符串相加
# str1 * time  字符串和整数相乘
# len()        统计字符串的长度
#

str1 = "This is a "
str2 = "short string."
sentence = str1 + str2
print("Output #18: {0:s}".format(str1+str2))
print("Output #18: {0:s}".format(sentence))  
print("Output #19: {0:s} {1:s} {2:s}".format("She is ", "very "*4, "Beautiful."))
m = len(sentence)
print("Output #20: the len of sentence is {0:d}".format(m))
      