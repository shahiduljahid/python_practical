import sys
# # print(sys.argv)
# print('Hello, ' + sys.argv[2])
# input()

counter = 0
for i in sys.argv:
    counter+=1
    print("argument{}:{}".format(counter,i))
