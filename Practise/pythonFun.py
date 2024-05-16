# array1= ['1','2','4','5']

# print(list(enumerate(array1)))

# for ele in enumerate(array1):
#     print(ele)

# for count,ele in enumerate(array1 ,200):
#     print(count,ele)    

    
# # next_ele = next(enumerate(array1))
# print(next(enumerate(array1)))
# print(next(enumerate(array1)))    

# L1 = ['a','b','c']
# l_iter = iter (L1)

# # print(next(l_iter))
# # print(next(l_iter))


# while True:
#     item = next(l_iter ,'end')
#     if item == 'end':
#         break
#     print(item)

# import time

# # initializing list
# l = [1, 2, 3, 4, 5]

# # Creating iterator from list
# l_iter = iter(l)

# print("[Using next()]The contents of list are:")

# # Iterating using next()
# start_next = time.time_ns()
# while (1):
# 	val = next(l_iter, 'end')
# 	if val == 'end':
# 		break
# 	else:
# 		print(val, end=" ")

# print(f"\nTime taken when using next()\
# is : {(time.time_ns() - start_next) / 10**6:.04f}ms")

# # Iterating using for-loop
# print("\n[Using For-Loop] The contents of list are:")
# start_for = time.time_ns()
# for i in l:
# 	print(i, end=" ")
# print(f"\nTime taken when using for loop is\
# : {(time.time_ns() - start_for) / 10**6:.04f}ms")

# L2 = [{12,'ddd',True},'bcc','cccc']
# ex = enumerate(L2)
# ss , item = next(ex)
# item = sorted(item ,key=str)
# s1,s2,s3 =item
# print(ss,s1,s2,s3)
# ss ,(s1,s2,s3) = next(ex)
# print(ss,s1,s2,s3)

