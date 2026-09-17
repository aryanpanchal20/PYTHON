num=int(input('Enter a number'))
temp=num

sum=0
rem=0

total=0

while num>0:

    rem=num%10
    num//=10

    fact=1

    for i in range(rem,0,-1):
        fact=fact*rem
        rem-=1
        
    total=total+fact


if(total==temp):
    print("Number is strong number")
else:
    print("number is not strong number")