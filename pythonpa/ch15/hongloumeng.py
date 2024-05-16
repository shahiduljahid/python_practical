import  jieba				#导入模块
txtfilepath = '红楼梦.txt'
with open(txtfilepath, encoding='utf-8') as f:#打开文件（文本读取模式）
    txt = f.read()			#读取文本文件的所有内容
words = jieba.cut(txt) 		#使用精确模式对文本进行分词
counts = {}				#通过键值对的形式存储词语及其出现的次数
for word in words:			#遍历所有词语，每出现一次其对应的值加1
    if  len(word) == 1:		#单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())				#将键值对转换成列表
items.sort(key=lambda x: x[1], reverse=True)	#根据词语出现次数从大到小排序
for i in range(5):						#i=0~4
    word, count = items[i]
    print("{0:<8}{1:>8}".format(word, count))	#输出出现频率最高的5个单词
