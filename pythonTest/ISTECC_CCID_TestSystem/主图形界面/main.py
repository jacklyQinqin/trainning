import tkinter as tk
from tkinter import  ttk

#自定义模块和方法
#导入信安测试系统模块
import  isteccTestSys

win = tk.Tk()
win.title("北京华大信安科技有限公司芯片测试统计系统")
win.geometry("1024x576+100+50") #1025x576是16:9的比例



#按键部分
#按键1.绝对地址布局.
button1 = tk.Button(win,text="功能1",command=isteccTestSys.func1,width=25,height=1)
#pack的放置方法.是居中放置.
button1.place(x=10,y=150)

button2 = tk.Button(win,text="功能2",command=isteccTestSys.func1,width=25,height=1)
#pack的放置方法.是居中放置.
button2.place(x=10,y=180)

button3 = tk.Button(win,text="功能3",command=isteccTestSys.func1,width=25,height=1)
#pack的放置方法.是居中放置.
button3.place(x=10,y=210)

button4 = tk.Button(win,text="功能4",command=isteccTestSys.func1,width=25,height=1)
#pack的放置方法.是居中放置.
button4.place(x=10,y=240)

button5 = tk.Button(win,text="功能5",command=isteccTestSys.func1,width=25,height=1)
#pack的放置方法.是居中放置.
button5.place(x=10,y=270)

button6 = tk.Button(win,text="功能6",command=isteccTestSys.func1,width=25,height=1)
#pack的放置方法.是居中放置.
button6.place(x=10,y=300)




#显示部分. 表格.
tree = ttk.Treeview(win)
tree.place(x=300,y=100)

#定义列
tree["columns"] = ("姓名","年龄","身高","体重")



#设置列.列还未显示
tree.column("姓名",width=100)
tree.column("年龄",width=100)
tree.column("身高",width=100)
tree.column("体重",width=100)




win.mainloop()