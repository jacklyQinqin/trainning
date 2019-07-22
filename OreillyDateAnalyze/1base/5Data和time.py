# -*- coding: utf-8 -*-

#!/usr/bin/python3
"""
data和time
是常用的功能。可以用来计算事件的间隔。周期。等许多参数。
Python含有datatime模组

常用的功能：
1. 日期
2. 日期和时间，时间精确到us。
3.
4.
5.
6.
7.
8.
"""
from datetime import  date , time ,datetime, timedelta

#日期功能
#date单纯的只有日期
#!s表示将强制转换为字符串，
today = date.today()
print(today)
print("Output #41: today: {0!s}".format(today)) #格式化输出1
print("Output #42: today: {0!s}".format(today.year))
print("Output #43: today: {0!s}".format(today.month))
print("Output #44: today: {0!s}".format(today.day))

#datetime含有日期和时间,精确到us
current_time = datetime.today()
print("Output #45: datatime: {0!s}".format(current_time))

#timedelta 时间间隔功能
#可以增加或者减去对应的时间间隔
#参数可以是 weeks days hours minutes second ms us .
#one_day = timedelta()
#print(one_day)
one_day = timedelta(days=1)
#print("Oneday = {0!s}".format(one_day))
yestoday =  today - one_day
print("Output #46:Yestoday :{0!s}".format(yestoday))
#计算小时
eight_hours = timedelta(hours=-8)
print("Output #47:{0!s},{1!s}".format(eight_hours.days,eight_hours.seconds))