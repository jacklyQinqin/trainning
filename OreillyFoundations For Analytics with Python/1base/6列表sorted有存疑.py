# -*- coding: utf-8 -*-

#!/usr/bin/python3
"""
列表是很常用的商业分析类型.
列表的每一个元素都是一个对象.可以是任意的类型!!!!
列表可以使用下标,列表是有顺序的.可以排序.
虽然列表的每一个元素,可以是任意的对象,但是常用的方法是一个列表,只收集一类元素.

常用的功能：
#1. 创建列表
    常用的几个方法
    len,min,nax,count
#2. 使用下标方法 < index value >来存取指定元素. 正方向从0 开始,反方向从-1开始.
#3. list slices. 列表的分割.
    可以获取列表的子集.从开始的index开始,到结束的index,且不包含结束的index的值.举例 [0:2] 包含 列表的[0] 和 [1]两个元素.不包含2.
    如果不包含开头index,就从0开始.
    如果不包含结束index,就到最后一项结束.
#4. copy a list list复制.
    使用 [:]即可.
#5. 连接/组合list
    使用 + 即可.
#6. 逻辑运算
    in
    not in
    这些逻辑运算除了计算数字之外,最重要的是用来判断是否已经具有了某个元素.这是在商业应用中非常重要的能力.可以增加有用的商业的逻辑.
    比如,判断是否已经添加了供应商列表,是否已经添加了某个人的资料等等.
    可以添加许多有用的逻辑判断.
#7.  元素的处理:增加,移除,POP.
    append  在list的最后添加一个元素
    pop     移除最后的一个元素
    remove  移除某个指定的元素.
    insert  在某个下标出插入指定的元素

#8. 逆序排列 reverse
    将所有的元素进行逆向排列.直接操作元素.
    如果需要保持原始的数据.先将原始文件拷贝.

#9. sort 排序.可以排序的有数字, 字符,数字打头的字符和数字,
    排序会直接操作列表.
    如果需要保持原始的数据.先将原始文件拷贝.
#10.sorted 列表中的列表排序.和 operator模组



#总结:
列表怎么用?用在哪里?常用的方法是啥?


"""

#1. 创建列表
a_list = [1,2,3]  #创建列表
print("Output #58:{}".format(a_list))
print("Output #59: {0} have {1} elecments".format("a_list",len(a_list)))#计算列表元素个数
print("Output #60: the maximum value in a_list is {}".format(max(a_list)))#计算列最大元素,必须是同类型的元素
print("Output #61: the minimum value in a_list is {}".format(min(a_list)))#计算列最小元素,必须是同类型的元素.
another_list = ['printer',5,5,['star','circle',9]]
print("Output #62: {}".format(another_list))
print("Output #63: {0} also have {1} elecments".format("another_list",len(another_list)))#计算列表元素个数
print("Output #64: 5 is in another_list {} time".format(another_list.count(5))) #计算某元素在列表中出现的次数
print("Output #64: ['star','circle',9] is in another_list {} time".format(another_list.count(['star','circle',9]))) #计算某元素在列表中出现的次数,如果没有.就返回0

#2. 使用下标方法 < index value >来存取指定元素. 正方向从0 开始,反方向从-1开始
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))

#3. list slices. 列表的分割.
print("#Output #73: {}".format(a_list[0:2]))
print("#Output #74: {}".format(a_list[:2]))
print("#Output #75: {}".format(another_list[1:]))

#4. copy a list list复制.
a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))

#5. 连接/组合list
a_longer_list = a_list + another_list
print("Output #78: {}".format(a_longer_list))

#6. 逻辑运算
#in和 not in
a = 2 in a_list
print("Output #79: {}".format(a))
if 2 in a_list:
    print("Output #80: 2 is in {}".format(a_list))
b = 6 not in  a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
    print("Output #82: 6 is not in {}".format(a_list))

#7.  元素的处理:增加,移除,pop,insert
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))
a_list.insert(1,100)
print("Output #85: {}".format(a_list))
a_list.remove(100)

#8 逆序排列 reverse
a_list.reverse()
print("Output #86: {}".format(a_list))
a_list.reverse()
print("Output #87: {}".format(a_list))

#9. sort 排序.可以排序的有数字, 字符
#unordered_list = [3,5,1,7,2,8,4,9,0,6]
#unordered_list = ['a','b','adf','1111g','u']
unordered_list = [5,1.2,8]
print("Output #88: {}".format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print("Output #89: {}".format(list_copy))

print("Output #90: {}".format(unordered_list))

#10.sorted 列表中的列表排序.
my_list = [[1,2,3,4],[2,4,3,1],[2,4,1,3]]
my_list_sorted_by_index_3 = sorted(my_list,key = lambda index_value:index_value[3])
print("Output #91: {}".format(my_list_sorted_by_index_3))
