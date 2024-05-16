def menu():    #显示菜单
    print("="*35)
    print("简易花名册程序")
    print("1.显示名字")
    print("2.添加名字")
    print("3.删除名字")
    print("4.修改名字")
    print("5.查询名字")
    print("6.退出系统")
    print("="*35)
names = []      # 创建存储花名册的列表对象
while True:     # 重复执行
    menu()      #显示菜单
    num = input("请输入选择的功能序号（1到6)：") #获取用户输入
    # 根据用户选择，执行相应的功能
    if num == '1':  #打印花名册清单
        print(names)
    elif num == '2':   #添加名字
        name = input("请输入要添加的名字：")
        names.append(name)  
        print(names)
    elif num == '3':    #删除名字
        name = input("请输入要删除的名字：")
        if name in names:
            names.remove(name)  
        else:
            print("系统中不存在名字：{}".format(name))
        print(names)
    elif num == '4':     #修改名字
        name = input("请输入要修改的名字：")
        if name in names:
            index = names.index(name)
            new_name = input("请输入修改后的名字：")
            names[index] = new_name  
        else:
            print("系统中不存在名字：{}".format(name))
        print(names)
    elif num == '5': #查询名字
        name = input("请输入要查询的名字：")
        if name in names:
            print("系统中存在名字：{}".format(name)) 
        else:
            print("系统中不存在名字：{}".format(name))
    elif num == '6':  #退出系统
        break
    else:          #只能输入1~6之间整数所对应的功能序号
        print("选项错误，请重新选择！")
