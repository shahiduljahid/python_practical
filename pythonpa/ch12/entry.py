from tkinter import *            #导入tkinter模块所有内容
root = Tk();  root.title("Entry")   #创建根窗口组件后设置窗口标题
v = StringVar()                #创建StringVar对象
w1 = Entry(root, textvariable=v)  #创建Entry组件对象
w1.pack()                    #显示单行文本框 
w1.get()                     #获取组件的内容
v.set('1234')                  #设置StringVar对象的值，组件文本自动更新
root.mainloop()               #调用mainloop()方法进入事件循环
