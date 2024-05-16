total = 0                     #累加和初值为0
for i in range(n):              #外循环i=0~n-1
    for j in range(n):          #内循环j=0~n-1
        total += a[i][j]        #累计和
print(total)                   #输出结果
