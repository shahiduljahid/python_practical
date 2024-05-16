import collections                   		#导入模块
def tail(filename, n=10):              		#返回文件最后n行内容
    '''Return the last n lines of a file'''
    with open(filename,encoding='utf-8') as f:	#打开文件（文本读取模式，指定编码）
        return collections.deque(f, n)  		#返回文件最后n行内容
if __name__=='__main__':           			#如果独立运行时，则运行测试代码
    path = r'deque_tail.py'          			#本示例程序
    dq = tail(path, n=2)             			#获取文件最后两行内容
    print(dq.popleft())         #倒数第二行内容
    print(dq.popleft())         #最后一行内容
