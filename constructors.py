# class employee:
#     def __init__(self,name,perct):
#         print("Hello constructor")
#         self.name=name
#         self.perct=perct

#     def show(self):
#         print("Hello show")
#         print("Name is : ",self.name)
#         print("Perct is : ",self.perct)

# emp1=employee("aryan",2.4)
# emp1.show()


#Private variable
# class employee:
#     def __init__(self,name,perct):
#         self.__name=name
#         self.__perct=perct

#     def show(self):
#        return self.__name
    
# emp1=employee("aryan",2.4)
# print("Name is ",emp1.show())


class employee:
    def __init__(self,name,perct):
        print("Hello constructor")
        self.name=name
        self.perct=perct


emp1=employee("aryan",2.4)



