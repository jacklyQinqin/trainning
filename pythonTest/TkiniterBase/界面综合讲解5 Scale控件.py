#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import tkinter
import time
win = tkinter.Tk()
win.title("scale控件")
win.geometry("400x400+200+40")

#供用户通过拖拽指示器来改变变量的值，可以水平，也可以竖直

#tkinter.HORIZONTAL水平
#tkinter.VERTICAL 竖直 (默认)
#length:水平表示宽度,竖直表示高度
#tickintervar:选择只将会为该数值的倍数.

scale1 = tkinter.Scale(win,from_=0,to=100,orient=tkinter.VERTICAL,tickinterval=10,length=300)

scale1.pack()

#设置值
scale1.set(20)

#取值
#print(scale1.get())

def showNum():
    print(scale1.get())
tkinter.Button(win,text="按钮",command=showNum).pack()

win.mainloop()
