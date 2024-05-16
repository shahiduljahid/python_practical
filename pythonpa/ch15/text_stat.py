import re					#导入模块
import collections				#导入模块
def analyze_text(text):			#定义函数
    paragraphs = re.split("\n\n", text)	#\n\n表示段落
    paragraph_count = len(paragraphs)	#统计段落数量
    print("段落数：{0}".format(paragraph_count))
    lines = re.split("\n", text)		#\n表示行数
    line_count = len(lines)			#统计行数
    print("行数：{0}".format(line_count))
    sentences = re.split("[.?!]", text)	#句子
    sentence_count = len(sentences)	#统计句子数量
    print("句数：{0}".format(sentence_count))
    words = re.split(r"\W+", text)		#单词
    word_count = len(words)		#统计单词数量
    print("单词数：{0}".format(word_count))
    freqs = collections.Counter(words)	#单词出现的频率
    print("频率最高的10个单词：")
    for (w, n) in freqs.most_common(10):
        print("{0:10}:{1:10}".format(w, n))
if __name__ == "__main__":		#如果独立运行时，则运行测试代码
    filename = "tomsawyer.txt"
    with open(filename,"r") as f:		#打开文件（文本读取模式）
        text = f.read()
    analyze_text(text.strip())
