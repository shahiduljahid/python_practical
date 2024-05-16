import tkinter as tk          #导入tkinter模块
def popup(event):           #事件处理函数
    menubar.post(event.x_root, event.y_root) #鼠标右键位置显示菜单
root = tk.Tk()                          #创建一个Tk根窗口组件
#创建菜单
menubar = tk.Menu(root)                 #创建菜单
menubar.add_command(label="Font")      #添加Font命令
menuedit = tk.Menu(menubar, tearoff=0)    #创建菜单menuedit
#menuedit作为层叠菜单添加到上下文菜单
menubar.add_cascade(label="Edit", menu=menuedit) 
menuedit.add_command(label="Copy")     #添加Copy命令
menuedit.add_command(label="Cut")       #添加Cut命令
menuedit.add_command(label="Paste")      #添加Paste命令
#创建界面
textEdit = tk.Text(root, width=40, height=10)  #创建Text组件
textEdit.pack()                          #调用pack()方法调整显示位置和大小
root.bind('<Button-3>', popup)             #绑定事件
#附加主菜单到根窗口
root.mainloop()                        #调用mainloop()方法进入事件循环
