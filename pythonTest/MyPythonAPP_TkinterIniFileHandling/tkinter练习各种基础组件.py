
#!usr/bin/env/python3
#Author ---qinxd
#company---istecc
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#导入tkinter 作为 tk
import  tkinter as tk
import  tkinter.messagebox



#第1步,实例化tk类作为对象.作为主窗口
windows  = tk.Tk()
#设置主窗口的参数.比如title和大小等.
#设置title
windows.title("华大信安IS32U系列SPI下载ini文件转换工具")
#设置窗口大小(几何图形)
#16:9  640x360  800x450   960x540
#16:10  640x400  800x500  960x600
windows.geometry("640x360")

#标签label
#实例化标签
#参数:1.标签的容器. bg为背景 font为字体. width为左右宽度,height为上下高度.单位为字符
tabel_1_value = tk.StringVar()
label_1 = tk.Label(windows,textvariable = tabel_1_value, bg="green",font=("Arial",12),width=30,height=2)
#放置标签. 1.  xx.pack() 2. xx.pltce()
label_1.pack()

#按钮button
#button是一个标准的Tkinter窗口部件.用来实现各种按钮.
#按钮可以包含文本或图像.
#按钮可以与一个python方法相关联.当按钮被按下,Tkinter自动调用相关联的函数或者方法.
#按钮只能显示一种字体.但是可以跨行.
#文本中的一个字母可以有下划线.例如标明一个快捷键.
#默认情况下,Tab键用于将焦点移动到一个按钮部件.
#简而言之,按钮部件用来让用户"马上执行某个任务"
#按钮通常在工具条或者应用程序窗口中,并且用来接收或者忽略输入在对话框中的数据.
#按钮可以和输入的数据配合.

#创建方式;制定按钮的内容(文本.位图,图像)和一个当按钮被按下时的回调函数即可.
#方法需要编写
on_hit = False
def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        tabel_1_value.set("you hit me")
        return
    else:
        on_hit = False
        tabel_1_value.set("")
        return
#生成按钮实例
button_1 = tk.Button(windows,text="确定",command=hit_me)
#放置
button_1.pack()




#Entry Tkinter的单行文本输入域.用来收集键盘的输入.类似Html中的text
#用于用户输入用户信息时,比如我们平时使用软件.登录网页时,用户交互界面输入登录信息.
#输入参数: 主窗口. 字体.显示格式.字体可以使用默认,不设置.
#使用pack放置位置,一般都是中轴对齐.

user_input_entry = tk.Entry(windows , show= None , font=("Arial",14))
password_input_entry = tk.Entry(windows , show='*', font=("Arial",14))
user_input_entry.pack()
#Entry.pack()


#Text窗口.是tkinter类中提供的一个多行文本区域.显示多行文本.可用来收集或显示用户输入的文字.
#类似于html的textarea.格式化文本显示.允许用不同样式和属性来显示和编辑文本.
#同时支持内嵌图像和窗口.
#什么时候用?
#在需要显示编辑用户,产品多行信息时.
def insert_point():#在鼠标焦点中国插入输入内容
    var = user_input_entry.get()
    t.insert("insert",var)

def insert_end():#在鼠标焦点中国插入输入内容
    var = user_input_entry.get()
    t.insert("end",var)

b1 = tk.Button(windows,text="当前插入",command = insert_point)
b2 = tk.Button(windows,text="最后插入",command = insert_end )
b1.pack()
b2.pack()
t = tk.Text(windows,height = 10,font=("alira",14))

#Listbox 列表框.



#RandioButton单选框



#CheckButton复选框





#Scale进度条
#可以用来表明当前进度.
#用户评级.程序加载或者处理进度等.
l = tk.Label(windows, bg="red",fg="white", width=20, text="empty")
l.pack()

def print_selection(v):
    l.config(text="You have choose "+v)
s = tk.Scale(windows,label="try me",from_=0,to=20,orient=tk.HORIZONTAL,length=200,showvalue=0,tickinterval=0.1,command=print_selection)
s.pack()



#Canvas画布.暂时用不到.




#meun菜单栏用来实现下拉菜单和弹出菜摊.点下菜单后弹出的一下选项列表.用户可以从中选择.
#什么时候用?提供菜单选项功能.
#关系:大容器内有小容器,就是菜单栏.小菜单内有菜单项.
#第10步定义一个函数,用来代表菜单选项的功能.
counter = 0
def do_job():
    global counter
    l.config(text="do" + str(counter))
    counter+=1
#第五步,创建一个菜单栏.我们可以理解成一个放在窗口上方的容器.
menubar = tk.Menu(windows)
#第六步:创建一个File菜单项.默认不下拉,下拉内容包括New,Open,Save,Exit功能项
filemenu = tk.Menu(menubar,tearoff = 0)
#将上面定义的空菜单,命名为File,放在菜单栏中,也就是装入那个容器中.也就是我们平时看到的下拉菜单的标题.比如File.
menubar.add_cascade(label="Edit",menu=filemenu)
#在File中加入New,Open,Save等小菜单.即我们平时看到的下拉菜单.
filemenu.add_command(label="New",command=do_job)
filemenu.add_command(label="Open",command=do_job)
filemenu.add_command(label="Save",command=do_job)
filemenu.add_separator() #添加分割线
filemenu.add_command(label="Exit",command=windows.quit)#调用tkinter自带的quit函数

#第七步.创建一个edit菜单.默认不下拉.内容包括Cut,Copy,Paste功能项.
editmenu = tk.Menu(menubar,tearoff=0)
#将上面定义的控菜单命名为Edit.放在菜单栏中.就是装入容器中.
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut",command=do_job)
editmenu.add_command(label="Copy",command=do_job)
editmenu.add_command(label="Paste",command=do_job)
#第八步创建二级菜单.也就是菜单项中的菜单.
submenu = tk.Menu(filemenu)  #制定上级菜单容器.
filemenu.add_cascade(label="Import",menu=submenu,underline=0) #给放入的菜单submeun命名.
#第九步.创建三级菜单命令,即菜单栏里的菜单栏.
filemenu.add_command(label="Submeun_1",command=do_job)
#第十一步.创建菜单栏完成后,配置让菜单栏menubar显示出来.
windows.config(menu=menubar)


#Frame框架.相当于在主的画面上分割一个小的区域作为独立区域.
#可以有多个.


#messageBox消息框.用来显示你应用陈谷的消息框.就是我们平时看到的弹窗.
#用来提示.需要一个触发功能来触发这个弹窗.
#几种常用的形式.

def  hit_me():
    #tkinter.messagebox.showinfo(title='Hi', message='你好！')  # 提示信息对话窗
    #tkinter.messagebox.showwarning(title='Hi', message='有警告！')  # 提出警告对话窗
    #tkinter.messagebox.showerror(title='Hi', message='出错了！')  # 提出错误对话窗
    #print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    #print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))  # return 'True', 'False'
    print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'
#使用按键触发.一个弹窗.
tk.Button(windows,text='hit me',bg='green',font=("Arial",14),command=hit_me).pack()
t.pack()

#palce方法.
#按照精确坐标放置.
tk.Label(windows,text="place方法",font=("Arial",20),).place(x=400,y=0,anchor="nw")
#tk.Label(windows, text='Pl', font=('Arial', 20), ).place(x=50, y=100, anchor='nw')
#主windows刷新.
windows.mainloop()


