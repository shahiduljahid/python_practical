from tkinter import *            #导入tkinter模块所有内容
root = Tk();  root.title("Listbox")  #创建根窗口组件后设置窗口标题
v = StringVar()                 #创建StringVar对象
v.set(('linux','windows','unix'))     #设置对象取值列表
lb = Listbox(root, selectmode=EXTENDED, listvariable = v)
lb.pack()                      #调用pack()方法调整显示位置和大小
for item in ['python','tkinter','widget']:
    lb.insert(END,item)         #添加列表项目
lb.curselection()               #选择项目的索引位置：('2', '3')
for i in lb.curselection():
    print(lb.get(i), end=' ')      #输出所选项目：unix python
root.mainloop()               #调用mainloop()方法进入事件循环
