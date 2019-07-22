import serial
from time import sleep
import  tkinter as tk
import serial
from time import sleep

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data



#检测串口是否存在
def com():
    ser=serial.Serial()
    i=1
    while i<30:
        name='COM'+str(i)
        ser.open
        try:
            ser.is_open
            ser = serial.Serial(name)
            ser.baudrate=9600
            print(name)
            return name
        except serial.serialutil.SerialException:
            pass
        i+=1

"""
if __name__ == '__main__':

    #打开串口
    serial = serial.Serial('COM3', 9600, timeout=0.5)  # /dev/ttyUSB0
    if serial.isOpen():
        print("open success")
    else:
        print("open failed")
    a = 1
    while True:
        a=a+1
        a= a % 0xff
        serial.write(a)  # 数据写回
        sleep(0.2)
        data = recv(serial)
        print("receive : ", data)
        serial.flushInput()

#        if data != b'':
#
       # serial.write(data)  # 数据写回
"""
if __name__ == '__main__':
    #检测接口功能测试通过
    #com()

    #主窗口大小
    windows = tk.Tk()
    windows.title("华大信安IS32U320A串口下载工具  版权所有:北京华大信安科技有限公司   wwww.istecc.com\n")
    windows.geometry("1440x810")

    #选择串口部分
    #包含串口检测功能, 实例化图形包括:下拉菜单选择,以及一个label上面写(端口号)和一个确认打开按钮.


    print("Output #1: 检测完毕!")
    windows.mainloop()