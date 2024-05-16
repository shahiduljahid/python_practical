def my_sum3(a, b, *c):          #各数字累加和
    total = a + b               
    for n in c:                 #循环迭代c中的各个元素n
       total = total + n         #将n累加到total
    return total                #返回total的值
print(my_sum3(1, 2))            #计算1+2
print(my_sum3(1, 2, 3, 4, 5))      #计算1+2+3+4+5
print(my_sum3(1, 2, 3, 4, 5, 6, 7))  #计算1+2+3+4+5+6+7
