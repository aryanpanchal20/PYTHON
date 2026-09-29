starter = ['Soup', 'French Fries', 'Spring Roll']
starterprice = [100, 120, 150]

maincourse = ['Pizza', 'Burger', 'Pasta']
mainprice = [250, 180, 220]

sweetdish = ['Ice Cream', 'Gulab Jamun', 'Brownie']
sweetprice = [100, 80, 150]

order = []
b = 1

while b == 1:

    print("\n========== FOOD MENU ==========")
    print("1. Starter")
    print("2. Main Course")
    print("3. Sweet Dish")
    print("===============================")

    choice = int(input("Select category: "))

    if choice == 1:
        listmenu = starter
        listprice = starterprice
        category = "Starter"

    elif choice == 2:
        listmenu = maincourse
        listprice = mainprice
        category = "Main Course"

    elif choice == 3:
        listmenu = sweetdish
        listprice = sweetprice
        category = "Sweet Dish"

    else:
        print("Invalid choice")
        continue

    print("\n==========", category, "==========")
    print("ORDERNO   ITEM             PRICE")

    j = 0
    o = 0

    for i in listmenu:
        print((o + 1), "       ", i, "       ", listprice[j])
        j = j + 1
        o = o + 1

    print("================================")

    on = int(input("Enter order number: "))

    order.append([listmenu[on - 1], listprice[on - 1]])

    print("One order placed")

    b = int(input("Do you want to order again? Press 1 for Yes, 0 for No: "))


print("\n========== YOUR ORDER ==========")

total = 0

for k in order:
    print(k[0], " ", k[1])
    total = total + k[1]

print("================================")
print("Total bill : ", total)