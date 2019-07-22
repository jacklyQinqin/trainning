"""
算术运算符
比较（关系）运算符
赋值运算符
逻辑运算符
位运算符
成员运算符
身份运算符
运算符优先级
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
参考资料1:
https://blog.csdn.net/qq_41235053/article/details/81704523
1、简单实例
2、Label控件
3、Button控件
4、Entry控件
5、点击按钮输出输入框中的内容
6、Text控件
7、带滚动条的Text
8、Checkbutton多选框控件
9、Radiobutton单选框
10、Listbox控件一
11、Listbox控件二
12、Listbox控件三
13、Listbox四
14、Scale控件
15、Spinbox控件
16、Menu顶层菜单
17、Menu鼠标右键菜单
18、Combobox下拉控件
19、Frame控件
20、表格数据
21、树状数据
22、绝对布局
23、相对布局
24、表格布局
25、鼠标点击事件
26、鼠标移动事件
27、鼠标释放事件
28、进入和离开事件
29、响应所有按键的事件
30、响应特殊按键事件
31、指定按键事件
32、组合按键事件

参考资料2:
https://blog.csdn.net/ahilll/article/details/81531587

参考资料3:
bilibili  小甲鱼python零基础入门 tkinter部分


参考资料4:
bilibili   千峰网络

参考资料5:


'''
#!/usr/bin/env python/
# -*- coding: utf-8 -*-

#界面的处理不必花里胡哨 .
#大多数的好的界面,其实都是由专业的美工来完成的.
#大多数的情况,自己需要的是功能.
#简介大方,实用.对自己更重要.
#界面编程总结分为以下几部分:
#.控件.
# 布局
# 事件

#套路1:
#1.创建主窗口.!


#STEP1 导入tkinter
import  tkinter as tk


#STEP2 创建主窗口
win = tk.Tk()  #创建主窗口
win.title("yudanqu") #设置标题
win.geometry("400x400+200+50")  #设置大小 和位置. 后面的+200 和+50是图形界面的位置.


#STEP3. 创建其他控件
#3.1 Label:标签控件.可以显示文本.
#win 父窗体
#text 显示的文本内容
#bg  背景颜色
#fg  字体颜色
#font 字体
#wraplength:指定text文本中多宽之后换行
#justify 设置换行之后的对齐格式
#anchor :位置 n 北  e 东 w 西 center 居中 还可以写在一起 ne 东北方向
label = tk.Label(win,text="this is a word",bg='pink',fg = "red",font = ("黑体",20),\
                 width=20,height=10,wraplength=100,justify="left",anchor="nw")
label.pack()


#LAST 进入消息循环
win.mainloop()
