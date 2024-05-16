def quickSort(a, low, high): #对列表a快速排序，列表下界为low，上界为high
    i = low        #i等于列表下界
    j = high       #j等于列表上界
    if i >= j:       #如果下界大于等于上界，返回结果列表a
        return a
    key = a[i]     #设置列表的第1个元素作为关键数据
    while i < j:    #循环直到i=j
        while i < j and a[j] >= key: #j开始向前搜索，找到第一个小于key的a[j]
            j = j-1  
        a[i] = a[j]
        while i < j and a[i] <= key:  #i开始向后搜索，找到第一个大于key的a[i]
            i = i+1 
        a[j] = a[i]
    a[i] = key               #a[i]等于关键数据
    quickSort(a, low, i-1)   #递归调用快速排序算法（列表下界为low、上界为i-1）
    quickSort(a, j+1, high)  #递归调用快速排序算法（列表下界为j+1、上界为high）
def main():
    a = [59,12,77,64,72,69,46,89,31,9]   #测试数据列表
    quickSort(a, 0, len(a)-1)            #调用快速排序
    print(a)                          #输出排序结果
if __name__ == '__main__': main()  #如果独立运行时，则运行测试代码
