# # i=1
# # while i<=3:
# #     j=1
# #     while j<=3:
# #         print("*" ,end=" ")
# #         j+=1
# #     print()
# #     i+=1

# # print()

# # for i in range(1,5):
# #     for j in range(1,5):
# #         print("*",end=" ")
# #     print()


# i=1
# while i<=3:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

# print()

# for i in range(1,4):
#     for j in range(1,4):
#         print("*",end=" ")
#     print()

n=4
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k+=1
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1

print()

for i in range(1,n+1):
    for k in range(1,((n-i)+1)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

    print()

for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)