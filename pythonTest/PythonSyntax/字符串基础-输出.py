# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:49:49 2019

@author: Administrator
"""

#string是最重要的一种python数据处理基础类型。
#主要作用是提示信息人机互动，也是文本处理的基础

#可以使用单引号 双引号 和三引号
#单引号
print("Output #14: {0:s}".format('I\'m enjoying lenaring python '))
#双引号可以多行文本，但是每行需要一个backslash。反斜杠
print("Output #15: {0:s}".format("This is a long string. Withouthe bakslash \
it would brun off the page on the ringth in the text editor and be very \
difficult to read and edit .By using the backslash you can split the long \
string  into smaller strings on separate lines so that the whole string is easy\
to view in the text editor.")) 
#三引号不需要反斜杠。内部可以写任意值。三引号包含三个单引号和三个双引号
print("Output #16: {0:s}".format('''You can use triple single quotes 
for multi-line comment string.'''))
print("Output #17: {0:s}".format("""You can also use triple double quotes 
for multi-line comment strings."""))