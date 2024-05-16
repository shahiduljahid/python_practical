import jieba							#导入模块
from wordcloud import WordCloud			#导入模块
excludes = ["什么","一个","我们","那里","你们","如今", "说道","知道","老太太","起来",
"这里","出来","他们","众人","自己","一面","太太", "只见","怎么","奶奶","两个","没有",
"不知","这个","听见", "几个", "姑娘","不是"]	#停用词列表
txtfilepath = '红楼梦.txt'
with open(txtfilepath, encoding='utf-8') as f:	#打开文件（文本读取模式）
    txt = f.read()						#读取文本文件的所有内容
    words = jieba.lcut(txt)      			#使用精确模式对文本进行分词
    words = [word for word in words if len(word)>1]	#去除单个词语
    newtxt = ' '.join(words)				#使用空格将分词结果拼接成文本
    wc = WordCloud(background_color="white", width=800, height=600,
        font_path="msyh.ttc",
        max_words=100, 
        max_font_size=80,
        stopwords = excludes)			#创建WordCloud对象
    wc.generate(newtxt)					#文本分词，生成词云图
    wc.to_file('红楼梦.png')				#词云图输出到图像文件
