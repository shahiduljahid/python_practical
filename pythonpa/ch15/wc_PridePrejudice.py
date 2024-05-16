from wordcloud import WordCloud		#导入模块
import numpy as np					#导入模块
from PIL import Image				#导入模块
mask1=np.array(Image.open("heart1.jpg")) #读取为np-array类型，传递给mask参数
with open('PrideAndPrejudice.txt', 'r', encoding='utf-8') as file:#打开文件读取
    text = file.read()				#读取文件内容
    wc = WordCloud(background_color="white", 
                    width=800, 
                    height=600,
                    max_words=100,
                    mask = mask1)	#创建WordCloud对象
    wc.generate(text)				#文本分词，生成词云图
    wc.to_file('傲慢与偏见.png')		#词云图输出到图像文件
