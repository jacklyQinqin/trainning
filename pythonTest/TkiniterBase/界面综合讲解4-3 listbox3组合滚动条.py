#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import time
import tkinter

win = tkinter.Tk()
win.title("listbox")
win.geometry("400x400+200+40")

lb = tkinter.Listbox(win,selectmode = tkinter.EXTENDED)
lb.pack()

#添加元素
for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd", "good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
    lb.insert(tkinter.END,item)

sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)


#配置
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
#额外给属性赋值
sc["command"] = lb.yview
win.mainloop()