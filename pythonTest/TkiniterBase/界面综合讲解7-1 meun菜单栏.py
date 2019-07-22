#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import tkinter
import time
win = tkinter.Tk()
win.title("菜单栏")
win.geometry("400x400+200+40")

#创建菜单条
meumbar = tkinter.Menu(win)
win.config(menu=meumbar)

def func():
    print("********")
#创建一个菜单选项 tearoff :虚线拆分可以单独把菜单栏分离出界面.
menu1 = tkinter.Menu(meumbar,tearoff=False)
#给菜单栏增加选项
for item in ['python','c','java','c++', 'c#','php','B','退出']:
    menu1.add_separator()
    menu1.add_command(label=item, command=func)

## 向菜单条上添加菜单选项
meumbar.add_cascade(label="语言",menu= menu1)

win.mainloop()