from tkinter import *            #导入tkinter模块所有内容
root = Tk()                    #创建一个Tk根窗口组件
from tkinter.simpledialog import * #导入tkinter模块中的子模块simpledialog
i = askinteger(title='请输入', prompt='请输入整数:',initialvalue=100)
f = askfloat(title='请输入', prompt='请输入实数:')
s = askstring(title='请输入', prompt='请输入字符串:')
