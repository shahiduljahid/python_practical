import tkinter as tk                             #导入tkinter模块
from tkinter import messagebox                   #导入子模块messagebox
class Application(tk.Frame):                      #定义GUI应用程序类，派生于Frame类
    def __init__(self, master=None):                #构造函数，master为父窗口
        tk.Frame.__init__(self, master)              #调用父类的构造函数
        self.grid()                               #调用grid()方法调整显示位置和大小
        self.createWidgets()                       #调用对象方法，创建子组件
    def createWidgets(self):                        #对象方法：创建子组件
        #标签
        self.lblTitle = tk.Label(self, text='个人信息调查') #个人信息调查标签
        self.lblName = tk.Label(self, text='姓名')       #姓名标签
        self.lblSex = tk.Label(self, text='性别')         #性别标签
        self.lblHobby = tk.Label(self, text='爱好')       #爱好标签
        #个人信息标签置于0行0列，跨4列
        self.lblTitle.grid(row=0, column=0, columnspan=4) 
        self.lblName.grid(row=1, column=0)        #姓名标签置于1行0列
        self.lblSex.grid(row=2, column=0)          #性别标签置于2行0列
        self.lblHobby.grid(row=3, column=0)        #爱好标签置于3行0列
        #文本框
        self.entryName = tk.Entry(self)             #创建姓名Entry文本框组件
        self.entryName.grid(row=1, column=1, columnspan=3) #姓名文本框置于1行1列
        #单选按钮
        self.vSex = tk.StringVar()                 #创建性别StringVar对象
        self.vSex.set('M')                        #设置初始值为男
        self.radioSexM = tk.Radiobutton(self, text="男", value='M', variable=self.vSex)
        self.radioSexF = tk.Radiobutton(self, text="女", value='F', variable=self.vSex)
        self.radioSexM.grid(row=2, column=1)     #男单选按钮置于2行1列
        self.radioSexF.grid(row=2, column=2)      #女单选按钮置于2行2列
        #复选框
        self.vHobbyMusic = tk.IntVar()         #创建音乐IntVar对象
        self.vHobbySports = tk.IntVar()         #创建运动IntVar对象
        self.vHobbyTravel = tk.IntVar()         #创建旅游IntVar对象
        self.vHobbyMovie = tk.IntVar()         #创建影视IntVar对象
        self.checkboxMusic = tk.Checkbutton(self, text="音乐", variable=self.vHobbyMusic)
        self.checkboxSports = tk.Checkbutton(self, text="运动", variable=self.vHobbySports)
        self.checkboxTravel = tk.Checkbutton(self, text="旅游", variable=self.vHobbyTravel)
        self.checkboxMovie = tk.Checkbutton(self, text="影视", variable=self.vHobbyMovie)
        self.checkboxMusic.grid(row=3, column=1)  #音乐复选框置于3行1列
        self.checkboxSports.grid(row=3, column=2)    #运动复选框置于3行2列
        self.checkboxTravel.grid(row=3, column=3)    #旅游复选框置于3行3列
        self.checkboxMovie.grid(row=3, column=4)    #影视复选框置于3行4列
        #创建“提交”按钮组件
        self.btnOk = tk.Button(self, text='提交', command=self.funcOK) 
        self.btnOk.grid(row=4, column=1, sticky=tk.E)    #提交按钮置于4行1列
        #创建“取消”按钮组件
        self.btnCancel = tk.Button(self, text='取消', command=root.destroy) 
        self.btnCancel.grid(row=4, column=3, sticky=tk.W)  #取消按钮置于4行3列
    def funcOK(self):                                 #定义提交事件处理程序
        strSex = '男' if (self.vSex.get()=='M') else '女'
        strMusic = self.checkboxMusic['text'] if (self.vHobbyMusic.get()==1) else ''
        strSports = self.checkboxSports['text'] if (self.vHobbySports.get()==1) else ''
        strTravel = self.checkboxTravel['text'] if (self.vHobbyTravel.get()==1) else ''
        strMovie = self.checkboxMovie['text'] if (self.vHobbyMovie.get()==1) else ''
        str1 = self.entryName.get() + ' 您好：\n'
        str1 += "您的性别是: " + strSex + '\n'
        str1 += '您的爱好是:\n' + strMusic + ' ' + strSports + ' ' + strTravel + ' ' + strMovie
        tk.messagebox.showinfo("个人信息", str1)        #弹出消息框
root = tk.Tk()                                        #创建一个Tk根窗口组件
root.title('个人信息调查')                              #设置窗口标题
app = Application(master=root)                         #创建Application的对象实例
app.mainloop()                                     #调用mainloop()方法进入事件循环
