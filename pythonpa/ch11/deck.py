import random                        	#导入模块
SUITS = ['Club', 'Diamond', 'Heart', 'Spade']	#花色（梅花、方块、红桃、黑桃）
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] #牌面大小
#生成一副扑克牌，每副扑克牌包含52张牌（大、小王除外）
deck = []                           	#一副扑克牌
for rank in RANKS:                  	#对牌面大小循环迭代
    for suit in SUITS:                 	#对花色循环迭代
        card = rank + ' of ' + suit       	#一张扑克牌
        deck += [card]               	#添加到一副扑克牌
#洗牌
n = len(deck)                         	#一副扑克牌包含的张数（52）
for i in range(n):                      	#对于每张扑克牌
    r = random.randrange(i, n)          	#r取i~n-1中的随机整数
    deck[r], deck[i] = deck[i], deck[r]		#两张扑克牌交换
for s in deck: print(s)                  	#输出一副扑克牌
