scores = []    #创建空列表，用于储存从文本文件中读取的成绩信息
txtfilepath = 'data.txt'                    #指定源数据文件（原始成绩信息）
with open(txtfilepath, encoding='utf-8') as f:  #打开文件
    for s in f.readlines():                 #读取并遍历文件行
       scores.append(int(s))             #将数据转换为整数后添加到成绩列表
result_filepath = 'result.txt'               #指定结果数据文件（成绩统计信息）
with open(result_filepath,'w', encoding='utf-8') as f:  #打开文件（写入模式，指定编码）
    f.write("成绩个数：{}\n".format(len(scores)))
    f.write("最高分：{}\n".format(max(scores)))
    f.write("最低分：{}\n".format(min(scores)))
    f.write("平均分：{}\n".format(sum(scores)/len(scores)))
