from tkinter import  *
#pack()方法把Widget加入到父容器中，并实现布局
#grid()可以实现更复杂的布局
class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.creatW()
    def creatW(self):
        self.helloLabel = Label(self,text="标签:helloWorld")
        self.helloLabel.pack()
        self.quitButton = Button(self,text="Quit",command=self.quit)
        self.quitButton.pack()


app = App()
app.master.title("我的tkinter框架")
app.mainloop()
#设置界面元素()