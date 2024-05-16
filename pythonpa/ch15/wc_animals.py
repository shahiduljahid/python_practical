from wordcloud import WordCloud			#导入模块
text = "dog cat fish bird cat cat dog cat cat dog monkey cat"
wc = WordCloud(background_color="white")	#实例化WordCloud对象
wc.generate(text)						#文本分词，生成词云图
wc.to_file("wc_animals.png")				#词云图输出到图像文件
