import collections, re                   #导入模块
path = r'c:\pythonpa\ch11\counterTest.py'   #本程序作为测试文件
with open(path, encoding='utf8') as f:      #打开文件（文本读取模式）
    words = re.findall(r'\w+', f.read().lower())#读取文本内容，转化为小写
    c = collections.Counter(words)        #统计各单词的计数
    print(c.most_common(5))            #最高计数的5个单词
