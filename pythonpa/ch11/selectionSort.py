def selectionSort(a):                 #选择排序
    for i in range(0, len(a)-1):        #外循环
        m = i                    #当前位置下标
        for j in range(i + 1, len(a)):   #内循环
            if a[j] < a[m]:          #查找最小值的位置
                m = j
        a[i], a[m] = a[m], a[i]       #元素交换
def main():
    a = [59,12,77,64,72,69,46,89,31,9]  #测试数据列表
    selectionSort(a)                 #调用选择排序
    print(a)                        #输出排序结果
if __name__ == '__main__': main() #如果独立运行时，则运行测试代码
