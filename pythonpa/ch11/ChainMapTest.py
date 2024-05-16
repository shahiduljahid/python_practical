import os, argparse                 #导入模块
from collections import *            #导入模块
defaults = {'color': 'red', 'user': 'guest'}  #字典
parser = argparse.ArgumentParser()    #创建ArgumentParser对象
parser.add_argument('-u', '--user')      #增加要解析的命令参数信息
parser.add_argument('-c', '--color')     #增加要解析的命令参数信息
namespace = parser.parse_args()      #解析命令行参数，生成对应的列表
command_line_args = {k:v for k, v in vars(namespace).items() if v}
combined = ChainMap(command_line_args, os.environ, defaults) #连接多个map
print(combined['color'])             #输出颜色信息
print(combined['user'])              #输出用户信息
