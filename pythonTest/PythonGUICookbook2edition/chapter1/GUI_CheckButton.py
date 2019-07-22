#!/usr/bin/python3




#=====================================
#imports
#=====================================
import  tkinter as tk
from tkinter import  ttk
#Creat instance
win = tk.Tk()


#Add a title .
win.title("Python GUI")


#Modified Button click Events Function.
def click_me():
    pass

    #action.configure(text='hello' + name.get() +'' + number.get())

#Adding a Text box Entry widget
ttk.Label(win,text="Enter a name").grid(column=0, row=0)

#Adding a text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)


#Adding a Button
action = ttk.Button(win, text="Click Me!",command=click_me)
action.grid(column=2,row=1)
#设置非使能 state='disabled'可以让按钮变灰色.
#action.configure(state='disabled')


#combobox 选择框 .给出默认的值.也可以自己写入值.
ttk.Label(win,text="Choose a number").grid(column=1,row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number ,state='readonly')
number_chosen['values']= (7,2,3,4,5,42,100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)
#可以通过增加readonly属性,限定选择端口不能输入,只能选择
number_chosen.configure(state='readonly')


#复选框
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disalbed', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='UnChecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text='Enabled', variable=chVarEn)
check3.select()

#sticky=tk.W 左对齐
check3.grid(column=2, row=4, sticky=tk.W)

name_entered.focus()

#Set Focus.
#设置焦点之后,输入框已经有了输入的竖线,可以直接输入
name_entered.focus()
#设置非使能 state='disabled'可以让按钮变灰色.
#name_entered.configure(state="disabled")




#Disable Resizing the GUI by passing in  False, True
#win.resizable(False,False)

#Disable Resizing the GUI y -dimension .and enable x - dimension,
#win.resizable(True,False)

#=====================================
#Start GUI
#=====================================
win.mainloop()

