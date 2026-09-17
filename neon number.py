i=int(input("Enter number to check whether it is neon "))

temp=i

rem=0
sum=0

while i>0:
    rem=i%10
    sum+=rem
    i//=10

print(sum)

if(temp%sum==0):
    print("Number is harshad number")
else:
    print("Number is not harshad number")