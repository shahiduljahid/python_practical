txtfilepath = 'temperatures12.txt'              		#指定数据文件（原始温度信息）
with open(txtfilepath, encoding='utf-8') as f:    		#打开文件（文本读取模式）
    ts = f.readlines()                      		#读取气温文件中所有内容
    temp_high = [int(t1) for t1 in ts[0].strip().split(",")]	#最高温度列表
    temp_low  = [int(t1) for t1 in ts[1].strip().split(",")]	#最低温度列表
    ht = max(temp_high)                			#最高温度
    ht_loc = temp_high.index(ht) + 1      			#最高温度所在日期
    lt = min(temp_low)                 			#最低温度
    lt_loc = temp_low.index(lt) + 1        			#最低温度所在日期
    print(f"12月{ht_loc}号最热, 最高温度为{ht}")
    print(f"12月{lt_loc}号最冷, 最低温度为{lt}")
    #构建日平均气温列表
    temp_average = [(temp_high[i] + temp_low[i])/2 for i in range(len(temp_high))]
    #构建日平均气温低于10度的列表（低于10度则值为1，否则值为0）
    t10 = [int(t<10) for t in temp_average]
    #（针对1和0列表）统计连续5天日平均气温低于10度的汇总值
    t10_m = [t10[i]+t10[i+1]+t10[i+2]+t10[i+3]+t10[i+4] for i in range(len(t10)-4)]
    #第一个连续5天日平均气温低于10度的汇总值（就是5）
    t10_5 = max(t10_m) 
    #第一个连续5天日平均气温低于10度的汇总值所在的日期
    t10_5_loc = t10_m.index(t10_5) + 1
    print(f"上海12月{t10_5_loc}日入冬，为冬季首日")
