from tkinter import *                #导入tkinter模块所有内容
root = Tk();  root.title("Checkbutton")  #窗口标题
v = StringVar()                     #创建StringVar对象
v.set('yes')             #设置默认值为'yes'，对应选择状态
w = Checkbutton(root, text="音乐", variable=v, onvalue='yes', offvalue='no')
w.pack()               #调用pack方法，调整其显示位置和大小
v.get()                #用户去选后，获取其值为'no'
root.mainloop()         #调用组件的mainloop方法，进入事件循环
