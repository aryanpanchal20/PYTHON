foodmenu = {
    1: {
        "Starter": {
            1: {"Masala Papad": 100},
            2: {"Paneer Tikka": 200},
            3: {"Veg Manchurian": 300}
        }
    },
 
    2: {
        "Main Course": {
            1: {"Biryani": 250},
            2: {"Paneer Butter Masala": 200},
            3: {"Naan": 50}
        }
    },

    3: {
        "Dessert": {
            1: {"IceCream": 100},
            2: {"Rasmalai": 120},
            3: {"Rabdi": 150}
        }
    }
}

selected=[];

while True:
    print("================MENU================")
    print("1.Starter")
    print("2.FOOD COURSE")
    print("3.DESSERT")
    print("4.EXIT")


    choice=int(input("Enter Your Choice"))

    if choice==4:
        break

     
    if choice==1:

        print("==================STARTER================")
        

        print("1",foodmenu[1]['Starter'][1])
        print("2",foodmenu[1]['Starter'][2])
        print("3",foodmenu[1]['Starter'][3])

        
        item=int(input("Enter Your Choice"))


        selected.append(foodmenu[1]["Starter"][item])

        print("Item Added")

        

    
    elif choice==2:

        print("================MAIN COURSE===============")

        print("1",foodmenu[2]['Main Course'][1])
        print("2",foodmenu[2]['Main Course'][2])
        print("3",foodmenu[2]['Main Course'][3])

        item=int(input("Enter Your Choice"))

        
        selected.append(foodmenu[2]["Main Course"][item])

        print("Item Added")

       

    
    elif choice==3:

        print("===============DESSERT=====================")

        print("1",foodmenu[3]['Dessert'][1])
        print("2",foodmenu[3]['Dessert'][2])
        print("3",foodmenu[3]['Dessert'][3])

        item=int(input("Enter Your Choice"))

        selected.append(foodmenu[3]["Dessert"][item])
        
        print("Item Added")


    else:
        print("Invalid Choice")



print("\n================ YOUR ORDER ================")

total=0

for item in selected:
    for name, price in item.items():
        print(name, "=", price)
        total=total+price

print("===============================")

print("Total Bill =",total)



# print("=================MENU===================")
# print("==================STARTER================")
# print(foodmenu[1]['Starter'][1]);
# print(foodmenu[1]['Starter'][2]);
# print(foodmenu[1]['Starter'][3]);
# print("================MAIN COURSE===============")
# print(foodmenu[2]['Main Course'][1]);
# print(foodmenu[2]['Main Course'][2]);
# print(foodmenu[2]['Main Course'][3]);
# print("===============DESSERT=====================")
# print(foodmenu[3]['Dessert'][1]);
# print(foodmenu[3]['Dessert'][2]);
# print(foodmenu[3]['Dessert'][3]);
