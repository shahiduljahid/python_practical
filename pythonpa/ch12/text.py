from tkinter import *            #导入tkinter模块所有内容
root = Tk();  root.title("Text")    #创建根窗口组件后设置窗口标题
w = Text(root, width=20, height=5) #创建文本框，宽20，高5
w.pack()                      #调用pack()方法调整显示位置和大小
w.insert(1.0, '工欲善其事，必先利其器。\n《论语·卫灵公》')
w.get(1.0)                    #'工'
w.get(1.0, END)               #'工欲善其事，必先利其器。\n《论语·卫灵公》\n'
root.mainloop()                #调用mainloop()方法进入事件循环
