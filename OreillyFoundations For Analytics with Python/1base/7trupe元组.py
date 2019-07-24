# -*- coding: utf-8 -*-

#!/usr/bin/python3
"""

#总结:
元组怎么用?用在哪里?常用的方法是啥?

"""

#1. 创建元组  元组使用 ()创建.常规方法 len  , + , * ,下标取值等.
my_tuple = ('x', 'y', 'z')
print("Output #93: {}".format(my_tuple))
print("Output #94: my_tuple has {} elements".format(len(my_tuple)))
print("Output #95: {}".format(my_tuple[-1]))
longer_tuple = my_tuple + my_tuple * 3
print("Output #96: {}".format(longer_tuple))

#2 unpack tuple. 使用左值直接分配元组的元素
one ,two, three = my_tuple
print("Output #97: {0} {1} {2}".format(one,two,three))
var1 = "red"
var2 = "robin"
print("Output #98: {} {}".format(var1,var2))
var1, var2 = var2, var1
print("Output #99: {} {}".format(var1,var2))

#3 tuple和list的相互转换.不会改变原始值.
my_list = [1,2,3]
my_tuple = ('x', 'y', 'z')
print("Output #100: {}".format(tuple(my_list)))
print("Output #100: {}".format(my_list))
print("Output #101: {}".format(list(my_tuple)))
print("Output #101: {}".format(my_tuple))