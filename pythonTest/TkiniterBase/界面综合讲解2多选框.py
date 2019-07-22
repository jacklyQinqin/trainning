#!/usr/bin/env python/
# -*- coding: utf-8 -*-

#3.7 多选框
#多选框原理上就是建立多个单个Checkbutton选框,并指向同一个函数处理.
#每个多选框对应一个布尔值.

import tkinter
win = tkinter.Tk()
win.title("python GUI 测试")
win.geometry("800x600+200+40")

def updata():
    message = ""
    if hobby1.get() == True:
        message += "monery\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "people\n"
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,message)

hobby1 = tkinter.BooleanVar()
#创建多选框
check1 = tkinter.Checkbutton(win,text="money",variable=hobby1,command=updata)
check1.pack()

hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win,text="money",variable=hobby2,command=updata)
check2.pack()

hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win,text="money",variable=hobby3,command=updata)
check3.pack()
text = tkinter.Text(win, width=50, height=5)
text.pack()
win.mainloop()