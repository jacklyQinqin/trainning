# -*- coding: utf-8 -*-

#!/usr/bin/python3
"""

#1. 创建字典
#2. 在一个字典中存取一个值. 需要使用key索引.
#3. copy()方法
#4. keys,values,and items. 键,值,和键值对本
    使用get获取方法.
    获取到的keys和values是list
    items是元组.
#5. 逻辑判断 in和not in 和get  三项操作针对key,而不是value
    in 和not in 只返回逻辑值
    get方法用来获取相应的value.如果获取不到,则返回None
    如果在key后面加入获取不到时返回的string,则返回相应的string
    print("Output #117: {!s}".format(a_dict.get("four","Not in this dict.")))
#6 排序 在Fondations for Analutics with Python 一书 page64.需要回头看.
    排序的方法是排序key或者value,如果是数字的话,还可以升序或者降序.

#总结:
字典是什么?有什么特性?字典怎么用?用在哪里?常用的方法是啥?
字典在本质上,属于一种包含了信息和唯一标志配对的列表.唯一标志叫做key. 信息就是value
可以字典化许多东西:比如产品,生产厂家,串号,产品号.卖价信息等.
字典又叫做   associative array 关联数组. key-value stores 键值对 等. 在其他编程语言中,也有叫hash表.哈希表.

字典和列表的差异:

1.list使用下标作为指引.index. 在字典中,存取个体,使用key,key可以是整数,字符串,或者其他的python对象.
这样的特性使得字典可以不使用连续数字作为索引,可以使用更有用的方式来mapping映射 到值.
2.列表有一个bulidin 的隐含的顺序.因为列表是使用下标作为索引的.列表中的元素是固定顺序的.
字典没有固定的顺序.
3.列表不能够直接通过不存在的下标索引(index)去分配一个值来创造一个新的元素.在字典中,可以通过新的key,来直接创建一个需要的元素.
换句话说,字典可以随时使用key来添加一个新值.列表需要通过固定的方法来添加.且必须是按照顺序.不能添加任意的索引值(下标).
4.因为没有索引值,通过键值搜索,所以搜索更快.


"""


#1. 创建字典
empty_dict = {}
a_dict =  {'one': 1, 'two':2, 'three':3}
print("Output #102: {}".format(empty_dict))
print("Output #103:a_dict has {!s} elements.".format(len(a_dict)))
another_dict = {'x':'printer','y':5,'z':['star','circle',9]}
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict also has {!s} elements".format(len(another_dict)))


#2. 在一个字典中存取一个值. 需要使用key索引.
print("Output #106: {}".format(a_dict['two']))
print("Output #107: {}".format(another_dict['z']))

#3. copy()方法
a_new_dict = a_dict.copy()
print("Output #108: {}".format(a_new_dict))

#4. keys,values,and items. 键,值,和键值对本身.
print("Output #109: {}".format(a_dict.keys())) #获取所有的key的列表    dict_keys(['one', 'two', 'three'])
print("Output #110: {}".format(a_dict.values())) #获取所有的值的列表.   dict_values([0, 2, 3])
print("Output #111: {}".format(a_dict.items()))  #返回键值对的元组 dict_items([('one', 0), ('two', 2), ('three', 3)])

#5. 逻辑判断 in和not in 和get  三项操作针对key,而不是value
if 'y' in another_dict:
    print("Output #114: y is a key in another_dict : {}".format(another_dict.keys()))
if 'c' not in  another_dict:
    print("Output #115: c is not a key in another_dict: {}".format(another_dict.keys()))
print("Output #116: {!s}".format(a_dict.get("three")))
print("Output #117: {!s}".format(a_dict.get("four","Not in this dict.")))

#6 排序 在Fondations for Analutics with Python 一书 page64.需要回头看.
print("Output #119: {}".format(a_dict))
dict_copy = a_dict.copy()
ordered_dict = sorted(dict_copy.items(),key=lambda  item:item[0])
print(ordered_dict)

