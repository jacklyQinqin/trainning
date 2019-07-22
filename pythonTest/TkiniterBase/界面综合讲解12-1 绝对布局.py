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

label1.place(x=10,y=10)
label2.place(x=50,y=50)
label3.place(x=100,y=100)




win.mainloop()