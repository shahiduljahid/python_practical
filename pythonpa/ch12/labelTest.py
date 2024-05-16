from tkinter import *                 #导入tkinter模块所有内容
root = Tk();root.title("Label示例")      #创建根窗口组件后设置窗口标题
w = Label(root, text="姓名")           #创建Label组件对象，显示文本为"姓名"
w.config(width=20, bg='black', fg='white') #设置宽度、背景色、前景色
w['anchor'] = E                      #设置停靠方式为右对齐
w.pack()                           #调用pack()方法调整显示位置和大小
root.mainloop()                     #调用组件mainloop()方法，进入事件循环
