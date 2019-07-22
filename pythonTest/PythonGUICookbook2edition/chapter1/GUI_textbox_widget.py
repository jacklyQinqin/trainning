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

#Adding a Label .
#方法1
#ttk.Label(win, text="A Label").grid(column=0, row=0)
#方法2错误示范
#a_label = ttk.Label(win, text="A Label").grid(column=0, row=0)
#方法2正确 推荐
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=1)

#ttk.Label(win, text="b Label").grid(column=0, row=1)

#Modified Button click Events Function.
def click_me():
    action.configure(text='hello' + name.get())

#Adding a Text box Entry widget
ttk.Label(win,text="Enter a name").grid(column=0, row=0)

#Adding a text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)


#Adding a Button
action = ttk.Button(win, text="Click Me!",command=click_me)
action.grid(column=1,row=1)



#Disable Resizing the GUI by passing in  False, True
#win.resizable(False,False)

#Disable Resizing the GUI y -dimension .and enable x - dimension,
#win.resizable(True,False)

#=====================================
#Start GUI
#=====================================
win.mainloop()

