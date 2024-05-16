import tkinter as tk                  #导入tkinter模块
class Application(tk.Frame):           #定义GUI应用程序类，派生于Frame类
    def __init__(self, master=None):   #构造函数，master为父窗口
        tk.Frame.__init__(self, master) #调用父类的构造函数
        self.grid()                 #调用pack()方法调整显示位置和大小
        self.createWidgets()         #调用对象方法，创建子组件
    def createWidgets(self):          #对象方法：创建子组件
        self.listboxLeft = tk.Listbox(self, width=10, height=6) #创建Listbox组件
        self.listboxLeft.insert(0, '北京', '天津', '上海', '重庆')  #插入列表数据
        self.listboxLeft.grid(row=0, column=0, rowspan=5)  #置于0行0列跨5行
        self.listboxRight = tk.Listbox(self, width=10, height=6) #创建Listbox组件
        self.listboxRight.grid(row=0, column=2, rowspan=5)  #置于0行2列跨5行
        #创建按钮组件
        self.btnToRight = tk.Button(self, text='   >   ', command=self.funcToRight)
        self.btnToRight.grid(row=1, column=1)          #置于1行1列
        self.btnToLeft = tk.Button(self, text='   <   ', command=self.funcToLeft)
        self.btnToLeft.grid(row=3, column=1)          #置于3行1列
    def funcToRight(self):
        '''定义事件处理程序：在右边列表框显示左边列表框选中的内容'''
        for item in self.listboxLeft.curselection(): 
            #将选中的内容插入到右边列表框
            self.listboxRight.insert(tk.END, self.listboxLeft.get(item))
        for item in self.listboxLeft.curselection(): 
            #从左边列表框中一一删除选中的内容
            self.listboxLeft.delete(item)
    def funcToLeft(self):
        '''定义事件处理程序：在左边列表框显示右边列表框选中的内容'''
        for item in self.listboxRight.curselection():
            #将选中的内容插入到左边列表框
            self.listboxLeft.insert(tk.END, self.listboxRight.get(item)) 
        for item in self.listboxRight.curselection(): 
            #从右边列表框中一一删除选中的内容
            self.listboxRight.delete(item) 
root = tk.Tk()                                   #创建一个Tk根窗口组件root
root.title('列表框')                               #设置窗口标题
app = Application(master=root)                    #创建Application的对象实例
app.mainloop()                                 #调用mainloop()方法进入事件循环
