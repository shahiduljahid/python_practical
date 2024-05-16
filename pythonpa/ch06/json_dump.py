import json                        #导入模块
urls={'baidu':'http://www.baidu.com/',
      'sina':'http://www.sina.com.cn/',
      'tencent':'http://www.qq.com/',
      'taobao':'https://www.taobao.com/'}  #定义URL地址数据对象
with open(r'c:\pythonpa\data.json', 'w') as f: #打开json文件（写入模式）
    json.dump(urls, f)    #将URL对象序列化为JSON字符串后写入到文件中
