import sys                #导入模块
lo = int(sys.argv[1])        #获取命令行参数argv[1]，并将其转换为整数
hi = int(sys.argv[2])        #获取命令行参数argv[2]，并将其转换为整数
for line in sys.stdin:        #循环，从标准输入中获取数据
    value = int(line)       #将数据转换为整数
    if (value >= lo) and (value <= hi): #如果所读取的数据位于指定范围
        print(str(value))    #将该值写入到标准输出
