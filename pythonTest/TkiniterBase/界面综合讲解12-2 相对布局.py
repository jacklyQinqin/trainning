#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import tkinter
from tkinter import  ttk
import time
win = tkinter.Tk()
win.title("绝对布局")
win.geometry("600x400+200+40")


label1 = tkinter.Label(win,text="good",bg="blue")
label2 = tkinter.Label(win,text="nice",bg="red")
label3 = tkinter.Label(win,text="cool",bg="green")
# 相对布局，窗体改变对控件有影响
label1.pack(fill=tkinter.Y, side=tkinter.LEFT)
label2.pack(fill=tkinter.X, side=tkinter.TOP)
label3.pack()
win.mainloop()