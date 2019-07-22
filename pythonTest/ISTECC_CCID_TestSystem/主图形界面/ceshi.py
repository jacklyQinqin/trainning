"""

{"排名": "1", "片名": "霸王别姬", "主演": "张国荣,张丰毅,巩俐", "上映时间": "1993-01-01(中国香港)", "评分": "9.6"}
{"排名": "2", "片名": "罗马假日", "主演": "格利高里·派克,奥黛丽·赫本,埃迪·艾伯特", "上映时间": "1953-09-02(美国)", "评分": "9.1"}
{"排名": "3", "片名": "肖申克的救赎", "主演": "蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿", "上映时间": "1994-10-14(美国)", "评分": "9.5"}
{"排名": "4", "片名": "这个杀手不太冷", "主演": "让·雷诺,加里·奥德曼,娜塔莉·波特曼", "上映时间": "1994-09-14(法国)", "评分": "9.5"}
{"排名": "5", "片名": "教父", "主演": "马龙·白兰度,阿尔·帕西诺,詹姆斯·肯恩", "上映时间": "1972-03-24(美国)", "评分": "9.3"}
{"排名": "6", "片名": "泰坦尼克号", "主演": "莱昂纳多·迪卡普里奥,凯特·温丝莱特,比利·赞恩", "上映时间": "1998-04-03", "评分": "9.5"}
{"排名": "7", "片名": "龙猫", "主演": "日高法子,坂本千夏,糸井重里", "上映时间": "1988-04-16(日本)", "评分": "9.2"}
{"排名": "8", "片名": "唐伯虎点秋香", "主演": "周星驰,巩俐,郑佩佩", "上映时间": "1993-07-01(中国香港)", "评分": "9.2"}
{"排名": "9", "片名": "千与千寻", "主演": "柊瑠美,入野自由,夏木真理", "上映时间": "2001-07-20(日本)", "评分": "9.3"}
{"排名": "10", "片名": "魂断蓝桥", "主演": "费雯·丽,罗伯特·泰勒,露塞尔·沃特森", "上映时间": "1940-05-17(美国)", "评分": "9.2"}
{"排名": "11", "片名": "乱世佳人", "主演": "费雯·丽,克拉克·盖博,奥利维娅·德哈维兰", "上映时间": "1939-12-15(美国)", "评分": "9.1"}

"""
import tkinter as tk
#


# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()

# import tkinter as tk
#
# class App(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#
# # create the application
# myapp=App()
#
# #
# # here are method calls to the window manager class
# #
# myapp.master.title("My Do-Nothing Application")
# myapp.master.maxsize(1024, 768)
# myapp.master.minsize(768, 512)
# # start the program
# myapp.mainloop()


#
# import tkinter as tk
# # create the application
# myapp=tk.Tk()
# # here are method calls to the window manager class
# myapp.title("My Do-Nothing Application")
# myapp.maxsize(1024, 768)
# myapp.minsize(768, 512)
# # start the program
# myapp.mainloop()

import  tkinter as tk
class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
# create the application
myapp=App()
# # here are method calls to the window manager class
#
myapp.master.title("测试系统")
myapp.master.maxsize(1024, 768)
myapp.master.minsize(768, 512)
# start the program
myapp.mainloop()




