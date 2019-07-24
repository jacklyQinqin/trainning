#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import time
import tkinter

win = tkinter.Tk()
win.title("Spinbox控件数值选择框")
win.geometry("400x400+200+40")


#Spinbox控件

v = tkinter.StringVar()

def updata():
    print(v.get())

#increment : 步长,默认为1.
#values 要输入一个元组,最好不好喝from和 to同时用.而且步长也没用.
#command 只要值改变就会执行updata方法


sp = tkinter.Spinbox(win,from_=0,to=100,increment=5,textvariable=v,command=updata())
sp.pack()

#
v.set(20)
print(v.get())

win.mainloop()
