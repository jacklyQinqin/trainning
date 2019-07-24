#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import time
import tkinter

win = tkinter.Tk()
win.title("listbox")
win.geometry("400x400+200+40")


#multiple 支持多选

lb = tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)
lb.pack()

for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
    lb.insert(tkinter.END,item)

win.mainloop()
