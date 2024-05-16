f1 = 1; f2 = 1
for i in range(1, 11):
    print(f1, f2, end=" ") 
    f1 += f2; f2 += f1
input()
