import tkinter as tk                #导入tkinter模块
from tkinter.filedialog import *      #导入tkinter模块中的子模块filedialog
from tkinter import messagebox     #导入tkinter模块中的子模块messagebox
import tkinter.scrolledtext as tst      #导入tkinter模块中的子模块scrolledtext
class Application(tk.Frame):         #定义GUI应用程序类，派生于Frame类
    def __init__(self, master=None):  #构造函数，master为父窗口
        super().__init__(master)    #调用父类的构造函数
        self.grid()               #调用grid()方法调整显示位置和大小
        self.createWidgets()       #调用对象方法创建子组件
        self.createMenu()         #调用对象方法创建菜单
        root['menu'] = self.menubar #附加主菜单到根窗口
        root.bind('<Button-3>', self.f_popup)  #绑定事件
    def createWidgets(self):                #对象方法：创建子组件
        #创建ScrolledText组件
        self.textEdit = tst.ScrolledText(self, width=80, height=20)
        self.textEdit.grid(row=0, column=0, rowspan=6) #置于0行0列跨6行
    def createMenu(self):                          #对象方法：创建菜单
        self.menubar = tk.Menu(root)               #创建主菜单栏menubar
        #创建子菜单
        self.menufile  = tk.Menu(self.menubar)       #创建菜单menufile 
        self.menuedit = tk.Menu(self.menubar, tearoff=0) #创建菜单menuedit
        self.menuhelp = tk.Menu(self.menubar, tearoff=0) #创建菜单menuhelp
        self.menubar.add_cascade(label='File', menu=self.menufile) #添加菜单项'File'
        self.menubar.add_cascade(label="Edit", menu=self.menuedit) #添加菜单项'Edit'
        self.menubar.add_cascade(label="Help", menu=self.menuhelp) #添加菜单项'Help'
        #添加菜单项
        self.menufile.add_command(label='New', command=self.f_new)   #File-New
        self.menufile.add_command(label='Open', command=self.f_open)  #File-Open
        self.menufile.add_command(label='Save', accelerator='^A', 
command=self.f_save)             #File-Save
        self.menufile.add_separator()                              #分隔符
        self.menufile.add_command(label='Exit', command=root.destroy) #File-Exit
        self.menuedit.add_command(label="Cut", command=self.f_cut)   #Edit-Cut
        self.menuedit.add_command(label="Copy", command=self.f_copy) #Edit-Copy
        self.menuedit.add_command(label="Paste", command=self.f_paste) #Edit-Paste
        self.menuhelp.add_command(label="About", command=self.f_about) #Help-About
    def f_new(self):                         #定义事件处理程序：File-New
        self.textEdit.delete(1.0, tk.END)        #清空Text组件的内容
    def f_open(self):                        #定义事件处理程序：File-Open
        self.textEdit.delete(1.0, tk.END)        #清空Text组件的内容
        fname = tk.filedialog.askopenfilename(filetypes=[('Python源文件','.py')])
        with open(fname, 'r', encoding= 'utf-8') as f1:  #打开文件（文本读取）
            str1 = f1.read()                      #读入文件内容
        self.textEdit.insert(0.0, str1)                #插入内容到Text组件
    def f_save(self):                        #定义事件处理程序：File-Save
        str1 = self.textEdit.get(1.0, tk.END)    #获取Text组件中全部内容
        fname = tk.filedialog.asksaveasfilename(filetypes=[('Python源文件','.py')])
        with open(fname, 'w', encoding= 'utf-8') as f1:  #打开文件
            f1.write(str1)      #将Text组件中全部内容写入文件
    def f_about(self):           #定义事件处理程序：Help-About
        tk.messagebox.showinfo('关于', '版本V 1.0.1')
    def f_cut(self):             #定义事件处理程序：Edit-Cut
        try:
            #获取选择的内容
            str1=self.textEdit.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.textEdit.clipboard_clear()         #清空剪贴板
            self.textEdit.clipboard_append(str1)    #附加到剪贴板
            self.textEdit.delete(tk.SEL_FIRST, tk.SEL_LAST)#删除所选内容
        except: pass
    def f_copy(self):                     #定义事件处理程序：Edit-Copy
        try:
            #获取选择的内容
            str1=self.textEdit.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.textEdit.clipboard_clear()         #清空剪贴板
            self.textEdit.clipboard_append(str1)    #附加到剪贴板
        except: pass
    def f_paste(self):              #定义事件处理程序：Edit-Paste
        #获取剪贴板内容
        str1 = self.textEdit.selection_get(selection='CLIPBOARD')
        #使用剪贴板内容替换所选内容，否则插入剪贴板内容
        try:
            self.textEdit.replace(tk.SEL_FIRST, tk.SEL_LAST, str1)
        except:
            self.textEdit.insert(tk.INSERT, str1)     #插入内容到当前位置
    def f_popup(self, event):                      #事件处理函数
        self.menuedit.post(event.x_root, event.y_root) #鼠标右键显示菜单
root = tk.Tk()                 #创建一个Tk根窗口组件
root.title('简易文本编辑器')     #设置窗口标题
app = Application(master=root)   #创建Application的对象实例
app.mainloop()                #调用mainloop()方法进入事件循环
