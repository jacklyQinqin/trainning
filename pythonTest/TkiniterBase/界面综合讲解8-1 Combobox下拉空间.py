#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import tkinter
from tkinter import  ttk
import time
win = tkinter.Tk()
win.title("菜单栏")
win.geometry("400x400+200+40")

#绑定变量
cv = tkinter.StringVar()
com = ttk.Combobox(win,textvariable=cv)

com.pack()

com["value"] = ("黑龙江","吉林","辽宁")
com.current(0)


#绑定事件.
def func(event):
    print(com.get())
    #print(cv.get())
com.bind("<<ComboboxSelected>>", func)


win.mainloop()