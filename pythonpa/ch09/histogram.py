import random, math					#导入模块
class Stat:                           	#定义类
    def __init__(self, n):              		#构造函数
        self._data = []                	#空列表
        for i in range(n):              	#i=0~n-1
            self._data.append(0)       	#列表所有元素值为0
    def addDataPoint(self, i):
        """增加数据点"""
        self._data[i] += 1
    def count(self):
        """计算数据点个数之和（统计数据点个数）"""
        return sum(self._data)
    def mean(self):
        """计算各数据点个数的平均值"""
        return sum(self._data)/len(self._data)
    def max(self):
        """计算各数据点个数的最大值"""
        return max(self._data)
    def min(self):
        """计算各数据点个数的最小值"""
        return min(self._data)
    def draw(self):
        """绘制简易直方图"""
        for i in self._data:             	#迭代列表中每个元素
            print('#'* i)              		#输出i个井字符号'#'
if __name__ == '__main__':   				#独立运行时则运行测试代码
    #随机生成100个位于0到9的整数
    st = Stat(10)                   		#调用函数
    for i in range(100):             		#i=0~99
        score = random.randrange(0,10)		#0~9之间的随机整数
        st.addDataPoint(math.floor(score))	#增加数据点
    print('数据点个数：{}'.format(st.count()))
    print('数据点个数的平均值：{}'.format(st.mean()))
    print('数据点个数的最大值：{}'.format(st.max()))
    print('数据点个数的最小值：{}'.format(st.min()))
    st.draw()  						#绘制简易直方图
