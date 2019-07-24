#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import time
import tkinter

win = tkinter.Tk()
win.title("菜单栏")
win.geometry("400x400+200+40")

#说明,右键单击出现菜单栏.
#和通用的区别在于.菜单条的处理.
#通用的创建菜单条之后. 直接使用  win.config(menu=meumbar).将其添加.


#菜单条
menubar  = tkinter.Menu(win)

#菜单选项
menu1 = tkinter.Menu(menubar, tearoff = False)
def func():
    print("**********")
# 给菜单选项添加内容(标签和对应的执行对象)
for item in ['python','c','java','c++', 'c#','php','B','退出']:
    if item == '退出':
        menu1.add_separator() #添加分割线
        menu1.add_command(label=item,command=win.quit)
    else:
        menu1.add_command(label=item,command=func)

#添加到菜单条
menubar.add_cascade(label="语言", menu=menu1)

def showMenu(event):
    menubar.post(event.x_root, event.y_root)

#<Button-1> 左键
#<Button-2> 中间键
#<Button-3> 右键

win.bind("<Button-2>", showMenu)


win.mainloop()