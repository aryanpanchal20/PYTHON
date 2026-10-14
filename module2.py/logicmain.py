from logic import *

while True:
    print("1.Factor\n2.Factorial")
    ch=int(input("Enter your choice"))

    if ch==1:
        n=int(input("Enter number to find factor : "))
        factor(n)
    elif ch==2:
         n=int(input("Enter number to find factor : "))
         factorial(n)

