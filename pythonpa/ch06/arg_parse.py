import argparse                        #导入模块
parser = argparse.ArgumentParser()        #创建ArgumentParser对象
parser.add_argument('--length', default=10, type=int, help='长度') #长方形的长，默认为10
parser.add_argument('--width', default=5, type=int, help='宽度') #长方形的宽，默认为5
args = parser.parse_args()    #调用parser对象方法parse_args()解析命令行参数，生成对应的列表
area = args.length * args.width  #计算长方形的面积
print('面积=', area)            #输出长方形的面积
