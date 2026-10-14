def factor(n):
    print("Factors are : ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i) 


def factorial(n):
    fact=1

    for i in range(1,n+1):
        fact=fact*i

    print("Factorial are : ",fact)
