from tkinter import *                #导入tkinter模块所有内容
root = Tk();  root.title("LabelFrame")  #创建根窗口组件后设置窗口标题
lf = LabelFrame(root, text="组1")       #创建LabelFrame组件对象
lf.pack()                            #调用pack()方法调整显示位置和大小
Button(lf, text="确定").pack(side=LEFT)  #“确定”按钮，左停靠
Button(lf, text="取消").pack(side=LEFT)  #“取消”按钮，左停靠
root.mainloop()                       #调用组件mainloop()方法，进入事件循环
