import sys          #导入模块
n = int(sys.argv[1])   #从命令行第一个参数中获取n的值
power = 1          #2的0~n次幂赋初值
i = 0              #计数赋初值
with open(r'c:\pythonpa\out.log', 'w') as f:  #打开文件（写入模式）
    sys.stdout = f       #指定标准输出重定向到文件out.log中
    while i <= n:       #0~n循环
        print(str(i), ' ', str(power)) #输出0~n以及2的0~n次幂的列表
        power = 2 * power      #计算2的0~n次幂
        i = i + 1               #计数加1
    sys.stdout = sys.__stdout__   #恢复标准输出为默认值
    print('done!')
