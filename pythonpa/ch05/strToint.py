intN=123456          #给定一个整数
total=0              #累加和total赋初值
for s in str(intN):  #将整数转换为字符串，利用for迭代字符串序列
    total += int(s)  #将字符转换为整数，进行各个位数上的数字累加
print(total)         #输出给定整数的各个位数上的数字累加和
    