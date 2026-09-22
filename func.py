# //len without len func
x=[10,20,30,40,50]


ct=0
for i in x:
    ct+=1

print(ct)

max=x[0]
for i in x:
    if i>max:
        max=i
print(max)

# sum=0
# for i in x

#even and odd withoutusing predefined func

even=[]
evensum=0
odd=[]
oddsum=0

arr=[1,2,3,4,5,6]

for i in arr:
    if i%2==0:
        even+=[i]
        evensum+=i
    else:
        odd+=[i]
        oddsum+=i
print(even)
print(odd)

#finding key without predefined func

arr1=[1,2,3,4,5,6,7,8,9]
flag=0
index=0
key=int(input("Enter key to find"))
for i in arr1:
    if i==key:
        print(f"key found at {index} index")
        flag=1
        break
    index+=1

if flag==0:
    print("Key not found")
