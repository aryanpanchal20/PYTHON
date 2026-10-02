food={
    "veg":
    {
        "masala":100,
        "abc":200,
        "def":300
    },
    "nonveg":
        {
            "xyz":500,
            "mno":700,
            "qrs":900
        }
};


for category,item in food.items(): 
        print(category)

        for item,price in item.items():
                print(item,"=",price)