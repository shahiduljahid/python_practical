try:
    f = open('mytext.txt', 'w')                   #打开文件（写入模式）
    while True:                              #一直循环
        s = input('请输入字符串（按Q结束）：') #提示用户输入字符串
        if s.upper() == 'Q': break                #按Q或者q结束输入
        f.write(s + '\n')     #否则，将字符串写入文件中，每个字符串一行
except KeyboardInterrupt:
    print('程序中断！（Ctrl-C）')
finally:
    f.close()                                 #关闭文件
