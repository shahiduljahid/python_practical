def printfilewithlineno(path):               #定义函数
    with open(path, 'r', encoding='utf8') as f:  #打开文件（读取模式，指定编码）
        lines = f.readlines()               #读取文件内容
    for idx, line in enumerate(lines):        #枚举可迭代对象
        print(idx, line)
if __name__ == '__main__':               #如果独立运行时，则运行测试代码
    thisfile = __file__                   #将本源代码文件作为测试文件
printfilewithlineno(thisfile)               #打印本源代码文件的行号和内容
