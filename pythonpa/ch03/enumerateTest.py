seasons = ['Spring', 'Summer', 'Autumn', 'Winter']   #一年四季的列表清单
for i, s in enumerate(seasons, start=1):            #start默认从0开始，现指定从1开始
    print("第{0}季节：{1}".format(i, s))
