#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import time
import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("Frame框架")
win.geometry("400x400+200+40")

#
#框架控件：在桌面上显示一个矩形区域，多作为一个容器控件
#可用来显示文本

frm = tkinter.Frame(win)
frm.pack()

# left
frm1 = tkinter.Frame(frm)
tkinter.Label(frm1,text="左上",bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm1,text="左下",bg="blue").pack(side=tkinter.TOP)
frm1.pack(side=tkinter.LEFT)

#right
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r, text="右上", bg="green").pack(side=tkinter.TOP)
tkinter.Label(frm_r, text="右下", bg="red").pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)

win.mainloop()