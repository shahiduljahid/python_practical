def bubbleSort(a):                       #冒泡排序
    for i in range(len(a)-1, 0,-1):           #外循环
        for j in range(i):                  #内循环
            if a[j] > a[j + 1]:              #大数往下沉
                a[j], a[j + 1] = a[j + 1], a[j]  #两数交换
def main():
    a = [2,97,86,64,50,80,3,71,8,76]         #测试数据列表
    bubbleSort(a)                        #调用冒泡排序
    print(a)                             #输出排序结果
if __name__ == '__main__': main()  #如果独立运行时，则运行测试代码
