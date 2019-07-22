
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

#创建元素
#STEP2 创建主窗口 .必须要
win = tk.Tk()  #创建主窗口
win.title("yudanqu") #设置标题
win.geometry("800x600+200+50")  #设置大小 和位置. 后面的+200 和+50是图形界面的位置.


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
#label = tk.Label(win,text="this is a word",bg='pink',fg = "red",font = ("黑体",20),\
                # width=10,height=10,wraplength=100,justify="left",anchor="ne")

#pack的放置方法.是居中放置.
#label.pack()

#3.2 按键 Button.
#按键需要一个回调函数
#回调函数定义
def func1():
    print("hello,world!\n")
#创建按钮

button1 = tk.Button(win,text="功能1",command=func1,width=10,height=10)
#pack的放置方法.是居中放置.
button1.pack()

#默认大小
#button2 = tk.Button(win,text="功能2:打印字符",command=lambda:print("bbbbbbbb"))
#设定大小
button2 = tk.Button(win,text="功能2:打印字符",command=lambda:print("bbbbbbbb"),width=10,height=10)
#pack的放置方法.是居中放置.
button2.pack()

#退出功能
#注意事项:command =  后面跟函数名.但是不是函数()
button3 = tk.Button(win,text="quit",command=win.quit)
button3.pack()


#3.3  Entry控件  入口控件
#作用一般是用来输入账号,密码.路径.指令等信息.用来给程序提供信息
#密文显示
entry1 = tk.Entry(win,show="*")  #show="*"可以用来表示输入密码
entry1.pack()
#明文显示
entry2 = tk.Entry(win,)  #显示明文.
entry2.pack()
#变量的绑定
e = tk.Variable()
entry3 = tk.Entry(win,textvariable=e)
entry3.pack()

#e就代表输入框这个对象
e.set("wewewewewewewe")
print(e.get())
print(entry3.get())

#3.4组合1 点击按钮输出输入框的内容
def showinfo():
    #获取输入的内容
    print(entry2.get())

button4 = tk.Button(win,text="entry2输入信息获取",command=showinfo)
button4.pack()

#3.5 text控件
#就是一个文本框.用于显示多行文本
#参数说明
#父窗口
#宽度
#高度  高度表示的是用来显示的行数
text = tk.Text(win, width = 30,height=10)
text.pack()
str = '''盖闻天地之数，有十二万九千六百岁为一元。将一元分为十二会，乃子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥之十二支也。每会该一万八百岁。且就一日而论：子时得阳气，而丑则鸡鸣；寅不通光，而卯则日出；辰时食后，而巳则挨排；日午天中，而未则西蹉；申时晡而日落酉；戌黄昏而人定亥。譬于大数，若到戌会之终，则天地昏蒙而万物否矣。再去五千四百岁，交亥会之初，则当黑暗，而两间人物俱无矣，故曰混沌。又五千四百岁，亥会将终，贞下起元，近子之会，而复逐渐开明。邵康节曰：“冬至子之半，天心无改移。一阳初动处，万物未生时。”到此，天始有根。再五千四百岁，正当子会，轻清上腾，有日，有月，有星，有辰。日、月、星、辰，谓之四象。故曰，天开于子。又经五千四百岁，子会将终，近丑之会，而逐渐坚实。易曰：“大哉乾元！至哉坤元！万物资生，乃顺承天。”至此，地始凝结。再五千四百岁，正当丑会，重浊下凝，有水，有火，有山，有石，有土。水、火、山、石、土谓之五形。故曰，地辟于丑。又经五千四百岁，丑会终而寅会之初，发生万物。'''
text.insert(tk.INSERT,str)

#3.6带滚动条的Text
#实际就是滚动条.+ text框
# 创建滚动条
scroll = tk.Scrollbar()

text1 = tk.Text(win, width=30, height=10)
# side放到窗体的哪一侧,  fill填充
scroll.pack(side=tk.RIGHT, fill=tk.Y)
text1.pack(side=tk.LEFT, fill=tk.Y)
# 关联
scroll.config(command=text1.yview)
text1.config(yscrollcommand=scroll.set)

text1.pack()
str = '''盖闻天地之数，有十二万九千六百岁为一元。将一元分为十二会，乃子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥之十二支也。每会该一万八百岁。且就一日而论：子时得阳气，而丑则鸡鸣；寅不通光，而卯则日出；辰时食后，而巳则挨排；日午天中，而未则西蹉；申时晡而日落酉；戌黄昏而人定亥。譬于大数，若到戌会之终，则天地昏蒙而万物否矣。再去五千四百岁，交亥会之初，则当黑暗，而两间人物俱无矣，故曰混沌。又五千四百岁，亥会将终，贞下起元，近子之会，而复逐渐开明。邵康节曰：“冬至子之半，天心无改移。一阳初动处，万物未生时。”到此，天始有根。再五千四百岁，正当子会，轻清上腾，有日，有月，有星，有辰。日、月、星、辰，谓之四象。故曰，天开于子。又经五千四百岁，子会将终，近丑之会，而逐渐坚实。易曰：“大哉乾元！至哉坤元！万物资生，乃顺承天。”至此，地始凝结。再五千四百岁，正当丑会，重浊下凝，有水，有火，有山，有石，有土。水、火、山、石、土谓之五形。故曰，地辟于丑。又经五千四百岁，丑会终而寅会之初，发生万物。'''

text1.insert(tk.INSERT, str)





#LAST 进入消息循环
win.mainloop()
