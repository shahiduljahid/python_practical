try:
    f = open("testfile.txt", "w")               #打开文件（写入模式）
    f.write("这是一个测试文件，用于测试异常!!") #将字符串写入文件中
    f1 = open("testfile1.txt", "r")             #打开文件（读取模式）
except IOError:
    print("没有找到文件或读取文件失败")
else:
    print("文件写入成功！")
finally:
    f.close()                                   #关闭文件

