import tkinter as tk                         #导入tkinter模块
class MyDialog:                            #自定义对话框
    def __init__(self, master):                 #构造函数
        self.top = tk.Toplevel(master)           #生成Toplevel组件
        self.label1 = tk.Label(self.top, text='版权所有') #创建标签组件
        self.label1.pack()          #调用pack()方法调整显示位置和大小
        self.label2 = tk.Label(self.top, text='V 3.0.0')   #创建标签组件
        self.label2.pack()          #调用pack()方法调整显示位置和大小
        #创建按钮
        self.buttonOK = tk.Button(self.top, text='OK', command=self.funcOk) 
        self.buttonOK.pack()        #调用pack()方法调整显示位置和大小
    def funcOk(self):
        self.top.destroy()            #销毁对话框
class Application(tk.Frame):           #定义GUI应用程序类，派生于Frame类
    def __init__(self, master=None):   #构造函数，master为父窗口
        super().__init__(master)     #调用父类的构造函数
        self.pack()                #调用pack()方法调整显示位置和大小
        self.createWidgets()        #调用对象方法创建子组件
    def createWidgets(self):         #对象方法：创建子组件
        #创建Button组件
        self.btnAbout = tk.Button(self, text="About", command=self.funcAbout)
        self.btnAbout.pack()      #调用pack()方法调整位置和大小
    def funcAbout(self):          #定义事件处理程序
        d = MyDialog(self)       #创建对话框
root = tk.Tk()                   #创建一个Tk根窗口组件root
root['width']=400; root['height'] = 50 #设置窗口宽、高
app = Application(master=root)     #创建Application的对象实例
app.mainloop()                  #调用mainloop()方法进入事件循环
