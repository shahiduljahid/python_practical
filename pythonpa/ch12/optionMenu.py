from tkinter import *            #导入tkinter模块所有内容
root = Tk();  root.title("选择项")  #创建根窗口组件后设置窗口标题
v = StringVar(root)              #创建StringVar对象
v.set('Python')                  #设置对象取值
om = OptionMenu(root,v,'Python','Perl','JavaScript','C#')
om['width']=10                 #宽度10
om['anchor']=W                #设置停靠对齐方式
om.pack()                     #调用pack()方法调整显示位置和大小
root.mainloop()                #调用mainloop()方法进入事件循环
