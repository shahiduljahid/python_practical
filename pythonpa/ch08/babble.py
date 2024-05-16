def babble(words, times = 1):  #声明函数babble，第二个参数指定了默认值
    print(words * times)
babble('Hello')    #调用函数babble，只指定了一个参数传给words，times使用默认值1
babble('Tiger ', 3)  #调用函数babble，传'Tiger '给words，传3给times
