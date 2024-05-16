from tkinter import *                 #导入tkinter模块所有内容
root = Tk();  root.title("Radiobutton")   #创建根窗口组件后设置窗口标题
v = StringVar();v.set('M')              #创建StringVar对象后设置初始值
w1 = Radiobutton(root, text="男", value='M', variable=v)
w2 = Radiobutton(root, text="女", value='F', variable=v)
w1.pack(side=LEFT)                #调用pack()方法调整显示位置
w2.pack(side=LEFT)                #调用pack()方法调整显示位置
v.get()                            #选择女后，获取其值：'F'
root.mainloop()                    #调用mainloop()方法进入事件循环
