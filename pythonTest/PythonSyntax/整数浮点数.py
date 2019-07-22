# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:21:46 2019
#Intergers
#注意打印的方式使用format
#
@author: Administrator
"""
#整数部分
x  = 9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4)) # 求幂 3*3*3*3  81 
print("Output #6: {0}".format(int(9.3)/int(2.7)))#类型转换。计算时舍弃小数部分
      #但是除法的结果没有舍弃 。9/2  = 4.5
print("Output #6: {0}".format(int(int(9.3)/int(2.7))))#类型转换。计算时舍弃小数部分
      #除法的结果没有舍弃 。相当于int(9/2)  = 4


#浮点数部分
#注意 format的格式 {参数:格式} 
    #.3f表示小数点后3位精度
print("Output #7: {0:.3f}".format(8.3/2.7))
y = 2.5 * 4.8
print("Output #8: {0:.1f}:".format(y))
r = 8 / float(3) #数据的浮点数转换
print("Output #9: {0:.2f}".format(r))
print("Output #10:{0:.4f}".format(8.0/3))
      