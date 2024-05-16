import os, re							#导入模块
def tasklist():							#定义函数
    regex_task = re.compile(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)')
    with os.popen('tasklist /nh', 'r') as f:			#打开文件（读取模式）
        for line in f:
            print(regex_task.findall(line.strip()))	#拆分字符串
if __name__=='__main__':					#如果独立运行时，则运行测试代码
    tasklist()							#调用函数
