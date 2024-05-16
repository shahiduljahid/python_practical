def insertSort(a):                      #插入排序
    for i in range(1, len(a)):            #外循环（1~N-1）
        j = i
        while (j > 0) and (a[j] < a[j-1]):  #内循环
            a[j], a[j-1] = a[j-1], a[j]    #元素交换
            j -= 1                  #继续循环
def main():
    a = [59,12,77,64,72,69,46,89,31,9]   #测试数据列表
    insertSort(a)                     #调用插入排序
    print(a)                         #输出排序结果
if __name__ == '__main__': main()  #如果独立运行时，则运行测试代码
