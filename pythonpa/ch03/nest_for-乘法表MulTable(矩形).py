#chapter03\nest_for.py
for i in range(1, 10):             #外循环
    s = ""
    for j in range(1, 10):         #内循环
        s += str.format("{0:1}*{1:1}={2:<2} ", i, j, i * j)
    print(s)
