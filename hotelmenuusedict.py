foodmenu = {
    1: {
        "Starter":{
                1: {"Masala Papad ":100},
                2: {"Paneer Tikka":200},
                3: {"Veg Manchurian":300}
        }
    },

    2:{
        "Main Course":{
            1: "Biryani",
            2: "Paneer Butter Masala",
            3: "Naan"
             
        }
    },

    
    3:{
        "Dessert":{
            1: "IceCream",
            2: "Rasmalai",
            3: "Rabdi"
             
        }
    },
}

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
    #    print("2",foodmenu[1]['Starter'][2])
     #   print("3",foodmenu[1]['Starter'][3])

        item=int(input("Enter Your Choice"))

        print("You selected",foodmenu[1]["Starter"][item])

    
    elif choice==2:

        print("================MAIN COURSE===============")

        print("1",foodmenu[2]['Starter'][1])
        print("2",foodmenu[2]['Starter'][2])
        print("3",foodmenu[2]['Starter'][3])

        item=int(input("Enter Your Choice"))

        print("You selected",foodmenu[2]["Starter"][item])

    
    elif choice==3:

        print("===============DESSERT=====================")

        print("1",foodmenu[3]['Starter'][1])
        print("2",foodmenu[3]['Starter'][2])
        print("3",foodmenu[3]['Starter'][3])

        item=int(input("Enter Your Choice"))

        print("You selected",foodmenu[3]["Starter"][item])

    else:
        print("Invalid Choice")

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
