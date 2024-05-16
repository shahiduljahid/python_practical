def unique(items):
    items_existed = set()      #创建一个空集合
    for item in items:         #对于列表中的每一项
        if item not in items_existed:  #如果列表中的该项不在当前集合中
            yield item   #生成器函数使用yield语句返回一个值，然后
#保存当前函数的整个执行状态，等待下一次调用
            items_existed.add(item) #将不重复元素item添加到集合中
if __name__ == "__main__":    #如果独立运行时，则运行测试代码
    a = [1, 8, 5, 1, 9, 2, 1, 10]  #存在重复项的列表
    a1 = unique(a)          #去除列表中的重复项（保持原来的顺序）
    print(list(a1))           #去除重复项后的列表内容
