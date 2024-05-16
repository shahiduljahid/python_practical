from tkinter import *            #导入tkinter模块所有内容
root = Tk()                    #创建一个Tk根窗口组件
from tkinter.simpledialog import * #导入tkinter模块中的子模块simpledialog
#创建SimpleDialog组件
dlg = SimpleDialog(root, text='继续？', buttons=['Yes','No','Cancel'], default = 0)
