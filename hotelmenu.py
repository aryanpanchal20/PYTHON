listmenu=['a','b','c']
listprice=[100,200,300]

order=[]
b=1

while b==1:
    j=0
    o=0
    print("ORDERNO  ITEM  PRICE")
    for i in listmenu:
        print((o+1),'       ',i,'   ',listprice[j])
        j=j+1
        o=o+1

    print("=========================================================")

    on=int(input('Enter order number'))
    order.append(on)
    print("One order placed")

    b=int(input("Do you want to order again press 1"))

print("Your order is ")
total=0
for k in order:
        print(listmenu[k-1],' ',listprice[k-1])
        total+=listprice[k-1]
print("Total bill : ",total)
