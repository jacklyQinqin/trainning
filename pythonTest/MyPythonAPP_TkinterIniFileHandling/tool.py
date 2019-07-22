
#!usr/bin/env/python3
#Author ---qinxd
#company---istecc
# -*- coding: utf-8 -*-

#导入tkinter 作为 tk
import  tkinter as tk
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:46:35 2018

@author: qinxd
"""

# 导入模块，可以接受输入参数作为打开的ini文件的名字
import sys

H_FILE = '''\
#ifndef __DOWNLOADFILE_H__
#define __DOWNLOADFILE_H__

//下载COS的函数
//0为正确
//将ini文本转换为数组之后,需要通过FOR循环进行下载
//unsigned char DownLoadArray(void);
//声明数组指针的外部引用
extern const char * arrayPointer[];
#endif

'''

C_FILE_START = '''
#include "DownloadFile.h"

//unsigned char DownLoad(void);
//将ini数据转换为数组后的数据文件

'''
C_FILE_END = '''

'''


def ShowPromptMessage():
    # ----------------------------------------------------------------------
    print("此脚本用来将IS32U512A的INI转换为数组形式,加入SPI格式的HEAD,LEN,XOR等信息")
    print("文件将输出到.\Output文件夹下")
    print("输出名字为:DownloadFile.c和DownLoadFile.h")
    print("")
    print("版本号:v0.2")
    print("作者:Qxd")
    print("更新时间:2018-10-25 16:30")
    print("版权所有:华大信安科技有限公司 www.itecc.com")
    print("开发时间:2018年10月24日")
    print("如有建议和需求请与作者联系:qinxd@istecc.com")
    print("内侧阶段仅限内部使用,请勿传播")
    # ---------------------------------------------------------------------


# 输入一行ini文件。然后返回处理好的数据
# 处理方式:1将，0x9000删除。
# 2.将APDU=删除。
# 3加头
# 4加长度
# 5加异或值
# 6转换为数组格式
def DealOneLineMessage(strOneLine):
    head = [0x40, 0x42, 0x53, 0x55]
    length = [0x00, 0x00, 0x00, 0x00]
    xorValue = [0x00]
    str1_list1 = strOneLine.split(',')
    str1_need = str1_list1[0].lstrip("APDU=")

    # print("#2:删除APDU=和,0x9000后的数据: {0:s}".format(str1_need))
    # 长度为 头  + 长度（4byte） + 数据 + xor
    length[0] = int(4 + 4 + 1 + (len(str1_need)) / 2)
    # print("#3:转换后的指令的总长度: {0}".format(hex(length[0])))

    # 将字符串转换为16进制list
    new_list = []
    for i in range(0, len(str1_need), 2):
        new_list.append(str1_need[i:i + 2])
    # print("#4:转换为list后的数据:  {0}".format(new_list))

    # 将字符串的list转换为数字,并计算异或值
    hex_value = []
    for str_element in new_list:
        hex_value.append((int(str_element, 16)))
    # print("#5:转换为数字类型后的数据: {0}".format(hex_value))
    xorValue[0] = head[0] ^ head[1] ^ head[2] ^ head[3] ^ length[0] ^ length[1] ^ length[2] ^ length[3]
    # 计算异或值
    for hex_element in hex_value:
        xorValue[0] ^= hex_element
    # print("#6:异或值为:{}".format(hex(xorValue[0])))

    # 将整个数据加上头，异或值，转换为字符串格式的数据形式
    # print(str1_need)
    new_list = head + length + hex_value + xorValue
    # print("#7:转换之后的指令: {0}".format(new_list))

    translate = []
    for elem in new_list:
        # print(str(hex(elem)))
        translate.append(str(hex(elem)))
        # print("#8:转换为list后的数据 {0}".format(translate))

    a = '{'
    b = '};\n'
    str1_need_return = ','.join(translate)
    str1_need_return = a + str1_need_return + b
    # print("#9:最终输出的数组为 {0}".format(str1_need_return))
    return str(str1_need_return)


def GenHFile():
    # print("在当前文件夹下产生一个固定文件名的.h文件")
    filewriter = open("DownLoadFile.h", 'w')
    filewriter.write(H_FILE)
    filewriter.close()


def GenCFile():
    print("hellowGEN")


# 主函数接口
# 方法1.
#######################
def main1():


    input_file = user_input_entry.get()
    #将路径的 \ 转换为 /
    input_file = str(input_file)
    input_file =  (input_file).replace("\\", "/")

    print(input_file)
    filereader =  open(input_file, 'r')

    filewrite = open("DownLoadFile.c", 'w')

    array_head = "const char downLoadArrayINDEX[] ="
    array_pointer = "downLoadArrayINDEX,\n"
    # 写入.C文件
    filewrite.write(C_FILE_START)

    # 写入转换后的数组
    count = 0
    for row in filereader:
        array = DealOneLineMessage(row.strip())
        array_head_index = array_head.replace('INDEX', str(count))
        array = array_head_index + array
        filewrite.write(array)
        count += 1
    filereader.close()

    # 写入数据指针
    filereader = open(input_file, 'r')
    count = 0  # 数据的数组计数
    array_head_list = "const char * arrayPointer[] = {\n"
    for row in filereader:
        array = DealOneLineMessage(row.strip())
        array_head_index = array_head.replace('INDEX', str(count))
        array_pointer_temp = array_pointer.replace('INDEX', str(count))
        array = array_head_index + array

        array_head_list = array_head_list + array_pointer_temp
        count += 1
    filewrite.write(array_head_list + '};\n')  # 写入数组的指针声明

    # 写入长度定义文件
    define_cmd = "#define MAX_LINE  " + str(count) + '\n'
    filewrite.write(define_cmd)
    filewrite.write(C_FILE_END)

    filereader.close()
    filewrite.close()
    # DealOneLineMessage()
    GenHFile()



# -----------------------------------------------------------------------------
##测试1开始
# str1  = "APDU=BF400100850000a2010020f12c0841093c8ae162bd20b85c70051f00f3116a12431382f60e2005ee3c00241c1201911008bfce0000f300ff01100506ff001a124340ff01336a6a081008a0a0960000ff20410211ff0102110218120f1912f071610412ee0452c804001215030900000e24000002770200b1c712000558015e01740411aa0d1d74082e6a,0x9000"
# print("#1:原始的测试数据{0:s}".format(str1))
# print("处理数据:")
# str1 = DealOneLineMessage(str1)
# print("处理后的数据为{}".format(str1))
##测试1结束
# ------------------------------------------------------------------------------


#第1步,实例化tk类作为对象.作为主窗口
windows  = tk.Tk()

#设置主窗口的参数.比如title和大小等.
#设置title
windows.title("华大信安IS32U系列SPI下载ini文件转换工具")
#设置窗口大小(几何图形)
#16:9  640x360  800x450   960x540
#16:10  640x400  800x500  960x600
windows.geometry("640x360")


#标签
#实例化标签
#参数:1.标签的容器. bg为背景 font为字体. width为左右宽度,height为上下高度.单位为字符
tk.Label(windows,text="请输入待转换的文件路径",font=("Arial",12),width=20,height=2).place(x=10,y=20,anchor='nw')

user_input_entry = tk.Entry(windows,show= None , font=("Arial",14))
user_input_entry.place(x=240,y=30,anchor='nw')

user_confirmation = tk.Button(windows,text="确认当前路径",command=main1)
user_confirmation.pack()

#放置标签. 1.  xx.pack() 2. xx.place()
#label_1.pack()

windows.mainloop()
