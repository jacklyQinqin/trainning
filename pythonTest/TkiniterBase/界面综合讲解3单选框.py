#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import tkinter
win = tkinter.Tk()
win.title("单选框")
win.geometry("800x600+200+40")


#3.8 单选框

#单选框.是多个框子只能选择一个.
#单选框所有的框子绑定同一个变量.这样就实现了单选.
#因为可能有多个单选,为了区分选择的对象,需要使用int变量.
#radio button 单选按钮




def updata():
    print("You get the radiobutton {0:d}".format(r.get()))
# 绑定变量，一组单选框要绑定同一个变量，就能区分出单选框了
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win,text = "one",value = 1,variable  = r, command=updata)
radio1.pack()
radio2 = tkinter.Radiobutton(win,text = "two",value = 2,variable  = r, command=updata)
radio2.pack()
radio3 = tkinter.Radiobutton(win,text = "three",value = 3,variable  = r, command=updata)
radio3.pack()


win.mainloop()