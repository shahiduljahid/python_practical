import jieba						#导入模块
from wordcloud import WordCloud		#导入模块
import numpy as np					#导入模块
from PIL import Image				#导入模块
mask1=np.array(Image.open("star.jpg"))	#读取为np-array类型，以传递给mask参数
txtfilepath = '2021政府报告.txt'
with open(txtfilepath, encoding='utf-8') as f:  #打开文件（文本读取模式）
    txt = f.read()				#读取文本文件的所有内容
    words = jieba.cut(txt)		#使用精确模式对文本进行分词
    words = [word for word in words if len(word)>1]  #去除单个词语
    newtxt = ' '.join(words)		#使用空格，将jieba分词结果拼接成文本
    wc = WordCloud(background_color="white", width=800, height=600,
                  font_path="msyh.ttc",
                  max_words=100,
                  mask = mask1, 
                  max_font_size=80)	#创建WordCloud对象
    wc.generate(newtxt)				#文本分词，生成词云图
    wc.to_file('2021政府报告.png')		#词云图输出到图像文件
