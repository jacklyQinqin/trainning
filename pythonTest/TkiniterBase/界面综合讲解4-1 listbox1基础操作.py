#!/usr/bin/env python/
# -*- coding: utf-8 -*-
import time
import tkinter

win = tkinter.Tk()
win.title("listbox")
win.geometry("800x600+200+40")


#listbox.列表框控件：可以包含一个或多个文本框
#list中的str参数,实际可以看做一个列表
#作用：在listbox控件的小窗口显示一个字符串

#创建一个listbox,添加几个元素
lb = tkinter.Listbox(win,selectmode = tkinter.BROWSE)
lb.pack()
#顺序插入
for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
    lb.insert(tkinter.END,item)
#插入到最前面
lb.insert(tkinter.ACTIVE,"cool")
#将列表作为一个元素添加
lb.insert(tkinter.END, ["very good", "very nice"])
#删除
#lb.delete(1,3)

#选中
lb.select_set(2,3)
# 取消选中：参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只取消第一个索引处的内容
#lb.select_clear(2)
#获取列表中的元素个数
print(lb.size())
#获取列表中的值.
print(lb.get(2,3))
#返回当前的索引值.从0 开始计数.
print(lb.curselection())


#判断是否选中
print(lb.select_includes(4))

win.mainloop()
