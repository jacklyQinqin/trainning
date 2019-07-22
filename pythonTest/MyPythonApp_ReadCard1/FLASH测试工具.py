#!usr/bin/env/python3
# Author ---qinxd
# company---istecc
# -*- coding: utf-8 -*-


# 导入PcscReader类
from PySmartCard.CpuCard import PcscReader
# 导入time模块
import time
import os
import datetime
import ctypes
import sys


listDownloadFIle = list()

# 循环次数
count = 0
# 通信界面类型： 1-contact reader   2-contactless reader
readerType = 1


def showLog(data, issend):
    if True:
        '''打印日志函数'''
        current = time.strftime('%Y_%m_%d %H:%M:%S', time.localtime())
        if issend:  # 发送到卡片的数据
            send = '-->'
        else:  # 卡片返回的数据
            send = '<--'
        print("{} {} {}".format(current, send, data))
        str1 = current +send + data +'\n'
        print(str1)
        f.write(str1)

def sendApdu(reader, apdu, recv_list, readerType=None):
    '''给卡片发送指令的函数'''
    # 清空
    recv_list[:] = []
    # 去掉多余的空格
    apdu = apdu.replace(' ', '')
    showLog(apdu, True)
    respone = reader.send_apdu(apdu, readerType)
    showLog(respone, False)
    # recv_list第1个元素是返回数据
    recv_list.append(respone[:-4])
    # recv_list第2个元素是sw
    recv_list.append(respone[-4:])


def sendApduCommand(reader, apdu, recv_list, readerType=None):
    '''完整的发送指令函数'''
    sendApdu(reader, apdu, recv_list, readerType)
    # 如果是返回的SW是6CXX或者61XX,重新发指令
    apdu = apdu.replace(' ', '')
    if recv_list[-1][:2] == '61':
        apdu = '00C00000' + recv_list[-1][2:4]
        sendApdu(reader, apdu, recv_list, readerType)
    elif recv_list[-1][:2].upper() == '6C':
        apdu = apdu[:8] + recv_list[-1][2:4]
        sendApdu(reader, apdu, recv_list, readerType)


# 读取下载的ini文件,并加入BF49000000引导指令.
def DownloadFile():
    # filenameAndPath = input("输入需要下载的文件和路径.\n")
    # filenameAndPath = filenameAndPath.replace('\\','/')
    startTime = datetime.datetime.now()
    print(filenameAndPath)
    with open(filenameAndPath, 'r') as f:
        listDownloadFIle[:] = []
        for i in f:
            i = i[5:-8]
            listDownloadFIle.append(i)
    # 加入引导
    # listDownloadFIle.append('BF49000000')
    for apdu in listDownloadFIle:
        # print(apdu)
        '''发送APDU'''
        # print('*' * 40)
        recv_list = []
        sendApduCommand(pcsc, apdu, recv_list, readerType)
        if recv_list[1] != "9000":
            print("Send Apdu Failed!")
    endTime = datetime.datetime.now()
    print("下载完成,耗时{0}".format(endTime.second - startTime.second))


'''实例化PCSC读卡器'''
pcsc = PcscReader()

'''获取所有的读卡器列表'''
readerName = pcsc.get_pcsc_readerlist()
##print(readerName)#字符串类型的读卡器名称，按;隔开
# 按;切割字符串，得到所有的读卡器名称
print('当前连接的读卡器有：')
readerNameList = readerName.split(';')
for i in range(len(readerNameList) - 1):
    print("{} {} :{}".format('reader', i, readerNameList[i]))

"""

"""
'''连接指定的读卡器'''
print('*' * 40)
# 要连接的读卡器



def sendApduTime(APDU,time):
    apdu = APDU
    while time:
        time -=1
        sendApduCommand(pcsc, apdu, recv_list, readerType)
        if recv_list[1] != "9000" or recv_list[0] != "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000":
            print("Send Apdu Failed!")
            f.write("Send Apdu Failed!\n")
            print("次数 ",i)
            while True:
                pass


# 下载DemoCos之后的设备名字
# useReaderName0 = "ISTECC 1002V2.0"
# useReaderName0 = "ISTECC 1302V1.0 0"
useReaderName0 = "HDXA IS32U512A_1.0 0"
useReaderName0 = "Beijing HuaDa Infosec IS32U512A 0"
if __name__ == '__main__':
    # 文件操作
    f = open("result.txt", "w")


    '''实例化PCSC读卡器'''
    pcsc = PcscReader()
    '''获取所有的读卡器列表'''
    readerName = pcsc.get_pcsc_readerlist()
    ##print(readerName)#字符串类型的读卡器名称，按;隔开
    # 按;切割字符串，得到所有的读卡器名称
    print('当前连接的读卡器有：')
    readerNameList = readerName.split(';')
    for i in range(len(readerNameList) - 1):
        print("{} {} :{}".format('reader', i, readerNameList[i]))

    print(readerNameList[0])

    #判断是否有cos
    # # 如果已经是下载了democos
    # if readerNameList[0] == 'Beijing HuaDa Infosec IS32U512A 0':
    #     while True:
    #         print("已经下载democos")
    #         time.sleep(2)
    # else:
    #     print("没有下载democos")

    # filenameAndPath = input("输入需要下载的文件和路径.\n")
    # filenameAndPath = filenameAndPath.replace('\\', '/')

    flag = True

    # 得到的是字符串类型的复位信息
    ATR = pcsc.connect_device(readerNameList[0])
    if ATR:
        print("ConnectDevice Success...")
        print("ATR: ", ATR)
    else:
        print("连接设备失败!")
        player = ctypes.windll.kernel32
        player.Beep(1000, 400)
        time.sleep(1)
        #continue

    while (flag):
        flag = False
        # 得到的是字符串类型的复位信息
        ATR = pcsc.connect_device(readerNameList[0])
        if ATR:
            print("ConnectDevice Success...")
            f.write("ConnectDevice Success...\n")
            print("ATR: ", ATR)
            f.write("ATR: "+ATR+'\n')
        else:
            print("连接设备失败!")

            player = ctypes.windll.kernel32
            player.Beep(1000, 400)
            time.sleep(1)
            continue

       # DownloadFile()


        recv_list = []
        # apdu = "BF450200083461731845045702"
        # sendApduCommand(pcsc, apdu, recv_list, readerType)
        # if recv_list[1] != "9000":
        #     print("Send Apdu Failed!")
        # apdu = "BFEE010F02"
        # sendApduCommand(pcsc, apdu, recv_list, readerType)
        # if recv_list[1] != "9000" or  recv_list[0] != "0F0F":
        #     print("Send Apdu Failed!")

        recv_list = []
        apdu = "BF09050000"
        sendApduCommand(pcsc, apdu, recv_list, readerType)
        if recv_list[1] != "9000":
            print("Send Apdu Failed!")

        apdu = "BF0C002040"
        sendApduCommand(pcsc, apdu, recv_list, readerType)
        if recv_list[1] != "9000":
            print("Send Apdu Failed!")

        count = 0
        while(count<10):

            #apdu = "BF0B00801051515151515151515151515151515151"
            #apdu = "BF0B004040112233445566778899AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00112233445566778899AABBCCDDEEFF00"
            apdu = "BF0B00204000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
            sendApduCommand(pcsc, apdu, recv_list, readerType)
            if recv_list[1] != "9000":
                print("Send Apdu Failed!")
                f.write("Send Apdu Failed!\n")
            sendApduTime("BF0C002040",1)
            print("完成次数",count)
            f.write("完成次数" + str(count) + '\n')
            count += 1



        '''上电'''
        print('*' * 40)
        # 通信界面类型： 1-contact reader   2-contactless reader
        # readerType = 1
        if 'Contactless'.lower() in useReaderName0.lower():
            readerType = 2
        if 0 == pcsc.power_on(readerType):
            print("Device PowerOn Success...")
        else:
            print("Device PowerOn Failed!")
        pcsc.disconnect_device()
        # time.sleep(1)

        # print(datetime.date.ctime)
