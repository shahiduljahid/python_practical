import tkinter as tk                     #导入tkinter模块
class Application(tk.Frame):             #定义GUI应用程序类，派生于Frame类
    def __init__(self, master=None):      #构造函数，master为父窗口
        super().__init__(master)        #调用父类的构造函数
        self.grid()                   #调用grid方法()调整显示位置和大小
        self.createWidgets()           #调用对象方法创建子组件
    def createWidgets(self):            #对象方法：创建子组件
        #创建Scale组件
        self.scaleFont = tk.Scale(self, from_=10, to=60, length=400,
             orient=tk.HORIZONTAL, command=self.changefont) 
        self.scaleFont.set(20)         #设置初始值
        self.scaleFont.pack()  #调用pack()方法调整显示位置和大小
        #创建Label组件
        self.lblTitle = tk.Label(self, text='Hello', font=('Helvetica', 20, 'bold'))
        self.lblTitle.pack()   #调用pack()方法调整显示位置和大小
    def changefont(self, value): #定义事件处理程序：改变字体
        fontNew = ('Helvetica', self.scaleFont.get(), 'bold')
        self.lblTitle.config(font=fontNew)
root = tk.Tk()                   #创建一个Tk根窗口组件
root.title('设置字体大小')          #设置窗口标题
root['width']=400; root['height'] = 50  #设置窗口宽和高
app = Application(master=root)      #创建Application的对象实例
app.mainloop()                   #调用mainloop()方法进入事件循环
