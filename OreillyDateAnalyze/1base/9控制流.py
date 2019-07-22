# -*- coding: utf-8 -*-

#!/usr/bin/python3
"""
是什么?有什么特性?怎么用?用在哪里?常用的方法是啥?
使用len产生序列的范围长度,再使用range产生一组序列,然后使用for或者while来进行迭代.
是常用的商业分析软件的使用方式
for i in range(len(squeue)):
    do something
"""

"""
控制流是什么?有什么特性?怎么用?用在哪里?常用的方法是啥?
"""


#1. if-else 用来进行2选1的判断
x = 0
if x>4 and x!=9:
    print("Output #124: {}".format(x))
else:
    print("Output #124: x is not greater than 4")

#2. if-elif-else 用来进行多选判断
x = 8
if x > 10:
    print("x is greater than 10")
elif x ==10:
    print("x is equal 10")
elif x>6 and x < 10:
    print("x is greater  than 6 and smaller than 9")
else:
    print("x < 6")

#3. for loops 迭代
y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', \
'Nov', 'Dec']
z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta', \
'Holly', 'Isabel', 'Jenny']
print("Output #126:")
#直接取值.
for month in y:
    print("{!s}".format(month))
print("Output #127:(index value :name in list)")
#下标索引. 0!s将数字字符化
for i  in range(len(z)):
    print("{0!s}:{1:s}".format(i,z[i]))
#用其他list的长度来索引自己的list
print("Output #128:(access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('J'):
        print("{!s}:{!s}".format(j,y[j]))
#循环迭代字典
another_dict = {'x':'printer','y':5,'z':['star','circle',9]}
for key ,value in another_dict.items():
    print("{0:s},{1}".format(key,value))


#4 while 迭代
print("Output #134:")
x = 0
while x < 11:
    print("{!s}".format(x))
    x += 1
#5简化的迭代方式.主要目的是简化程序.
#方式是加入括号方法和条件判断,来直接获取字典,列表,元组的子集.
#list 列表
my_data = [[1,2,3],[4,5,6],[7,8,9]]
row_to_keep = [row for row in my_data if row[2]>5] #在[] 内加入for 循环 和判断条件.会返回符合条件的list元素.生成一个列表
print("Output #130 (list comperhension): {}".format(row_to_keep))
#set 集合化元素
my_data = [(1,2,3),(4,5,6),(7,8,9),(7,8,9)]
set_of_tuples1 = {x for x in my_data}  #{}表示集合的方式.会自动的剔除重复项.生成一个集合.{ }
print("Output #131(set comprehension): {}".format(set_of_tuples1))
#从一个大字典中,通过筛选条件生成一个字典
my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
my_results = {key:value for key,value in my_dictionary.items() if value >10}
print("Output #133 (dictionary comprehension) :{}".format(my_results))