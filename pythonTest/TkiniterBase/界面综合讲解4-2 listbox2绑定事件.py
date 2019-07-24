#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import time
import tkinter

win = tkinter.Tk()
win.title("listbox")
win.geometry("800x600+200+40")

#绑定变量

lbv = tkinter.StringVar()

#与BORWSE相似,但是不支持鼠标按下后移动选中位置.
lb = tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
lb.pack()

#添加元素
#顺序插入
for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
    lb.insert(tkinter.END,item)

#打印当前
print(lbv.get())

# 设置选项
# lbv.set(("1","2","3"))

#绑定事件
#设置绑定值.
def myprint(event):
    print(lb.curselection())
    print(lb.get(lb.curselection()))#返回值.
lb.bind("<Double-Button-1>",myprint) #左键双击事件

win.mainloop()




