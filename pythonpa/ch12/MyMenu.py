import tkinter as tk                #导入tkinter模块
def f_print():
    tk.messagebox.showinfo('信息', '打印功能')
root = tk.Tk()                    #创建一个Tk根窗口组件
#创建主菜单栏
menubar = tk.Menu(root)            #创建主菜单栏menubar
#创建子菜单
menufile  = tk.Menu(menubar)        #创建菜单项menufile
menuedit = tk.Menu(menubar, tearoff=0) #创建菜单项menuedit
menuhelp = tk.Menu(menubar, tearoff=0) #创建菜单项menuhelp
menuTest = tk.Menu(menubar)         #创建菜单项menuTest
#menufile作为层叠菜单添加到主菜单栏
menubar.add_cascade(label='File', menu=menufile) 
#menuedit作为层叠菜单添加到主菜单栏
menubar.add_cascade(label="Edit", menu=menuedit) 
#menuhelp作为层叠菜单添加到主菜单栏
menubar.add_cascade(label="Help", menu=menuhelp) 
#menuTest作为层叠菜单添加到主菜单栏
menubar.add_cascade(label="菜单2", menu=menuTest) 
#在菜单menufile中添加菜单项
menufile.add_command(label='Open')     #添加菜单项Open
menufile.add_command(label='Save')     #添加菜单项Save
#添加菜单项Print
menufile.add_command(label='Print', accelerator='^P', command=f_print)
menufile.add_separator()               #添加分隔符
menufile.add_command(label='Exit')     #添加菜单项Exit
#在菜单menuedit中添加菜单项
menuedit.add_command(label="Cut")    #添加菜单项Cut
menuedit.add_command(label="Copy")   #添加菜单项Copy
menuedit.add_command(label="Paste")   #添加菜单项Paste
#在菜单menuhelp中添加菜单项
menuhelp.add_command(label="About")  #添加菜单项About
#在菜单menuTest中添加菜单项
menuTest.add_command(label="菜单项1")      #添加菜单项1
menuTest.add_command(label="菜单项2")       #添加菜单项2
menuTest.add_separator()                      #添加分隔符
#添加复选框菜单项1
menuTest.add_checkbutton(label="复选框菜单项1")
#添加复选框菜单项2
menuTest.add_checkbutton(label="复选框菜单项2")
menuTest.add_separator()                      #添加分隔符
#添加单选按钮菜单项1
menuTest.add_radiobutton(label="单选按钮菜单项1")
#添加单选按钮菜单项2
menuTest.add_radiobutton(label="单选按钮菜单项2")
menuTest.add_separator()                   #添加分隔符
menusub = tk.Menu(menuTest)               #创建子菜单
#menusub作为层叠菜单添加到菜单中
menuTest.add_cascade(label="子菜单", menu=menusub) 
menusub.add_command(label="子菜单项1")    #添加子菜单项1
menusub.add_command(label="子菜单项2")    #添加子菜单项2
#附加主菜单到根窗口
root['menu'] = menubar                    #附加主菜单到根窗口
root.mainloop()                          #调用mainloop()方法进入事件循环
