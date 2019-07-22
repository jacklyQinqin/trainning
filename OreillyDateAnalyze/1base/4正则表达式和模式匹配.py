# -*- coding: utf-8 -*-

#!/usr/bin/python3
"""
许多商业应用分析依赖于模式匹配。
python中提供re模块。提供了非常有效的搜索匹配模式

搜寻
"""
from math import exp,log,sqrt
import re

#count the number of times a pattern appears in a string.
string  = "the quic brown fox jumps over the lazy dog"
string_list = string.split()
pattern = re.compile("The",re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count+=1
print("Output #38: {0:d}".format(count))


