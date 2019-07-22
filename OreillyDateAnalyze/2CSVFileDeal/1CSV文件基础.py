# -*- coding: utf-8 -*-

#!/usr/bin/python3
"""
什么是CSV文件?
使用, 分隔的文本文件.易处理,好传输.
excel和任何文本处理程序都能处理.

注意事项:
脏数据.是数据文件中常有的数据.比如传感器出错.
比如类型错误.手工录入错误等.

除了正确的方法.
多记录错误.以及分析为什么会产生错误.一个人的专业程度和他遇到的错误多少成正比.

How Basic String Parsing Can Fail ?
    1.包含了多余的 ,



可以使用两种方法:
    1.使用built-in的 open write read等方法来操作.
    2.使用 pandas模组.
在实际应用中,最好用pandas模组.
"""


import sys
import pandas as pd

#接收三个参数. 参数0 当前py文件名  参数1 输入文件 参数2 输出文件
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)  #读取CSV文件
print(data_frame)  #打印数据
data_frame.to_csv(output_file,index = False)  #拷贝数据到另外一个CSV文件.
