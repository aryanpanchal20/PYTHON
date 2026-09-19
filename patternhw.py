#hour glass
n = 5

for i in range(1, n + 1):

    
    for j in range(i):
        print("*", end=" ")

    
    for j in range(2 * (n - i)):
        print(" ", end=" ")

   
    for j in range(i):
        print("*", end=" ")

    print()



for i in range(n, 0, -1):

    
    for j in range(i):
        print("*", end=" ")

    
    for j in range(2 * (n - i)):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()

print("==================================================================================")



for i in range(1, n + 1):

    
    for j in range(n - i):
        print(" ", end=" ")

    
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()



for i in range(n - 1, 0, -1):

    
    for j in range(n - i):
        print(" ", end=" ")

    
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

print("==================================================================================")

n = 5

for i in range(n):
    for j in range(n):
        if (i == 0 and j == 2) or \
           (i == 1 and (j == 1 or j == 3)) or \
           (i == 2) or \
           (i == 3 and (j == 0 or j == 4)) or \
           (i == 4 and (j == 0 or j == 4)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("=======================================================================================")
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("============================================================================================")

n = 5

# Upper half
for i in range(1, n + 1):

    # Spaces before stars
    for j in range(n - i):
        print(" ", end="")

    # Border
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()


# Lower half
for i in range(n - 1, 0, -1):

    # Spaces before stars
    for j in range(n - i):
        print(" ", end="")

    # Border
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")

    print()