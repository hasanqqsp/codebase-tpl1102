# 1 * 3 * 5 
# dst
x = 6
# for i in range(1,x+1):
#     for j in range(1,x+1):
#         # print(5 * (i-1))
#         if j % 2 == 1:
#             print(5 * (i-1) + j, end=" ")
#         else:
#             print("*",end=" ")
#     print()

for i in range (1, x**2 + 1):
    if (i % 2 == 1):
        print(i,end=" ")
    else:
        print("*",end=" ")
    if i % x == 0:
        print()