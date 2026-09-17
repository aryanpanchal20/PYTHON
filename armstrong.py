num=int(input("Enter a number"))
temp=num
sum=0
count=0
rem=0

while num>0:
    count+=1
    num//=10

num=temp
while num>0:
    rem=num%10
    sum+=rem ** count
    num//=10

if temp==sum:
    print("Number is armstrong")
else:
    print("Number is not armstrong")

