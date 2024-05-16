import json                         #导入模块
with open(r'c:\pythonpa\data.json', 'r') as f: #打开json文件（读取模式）
    urls = json.load(f)  #从文件中读取JSON字符串并反序列化后返回该对象
    print(urls)        #打印URL地址
