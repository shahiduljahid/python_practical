#chapter03\if_3desc2.py

a = int(input("请输入整数a："))
b = int(input("请输入整数b："))
c = int(input("请输入整数c："))
if (a < b):
    a,b=b,a    #a和b交换，使得a>b
if (a < c):
    a,c=c,a    #a和c交换，使得a>c
if (b < c):
    b,c=c,b    #b和c交换，使得b>c
print("排序结果（降序）：", a, b, c)


