# CONSTRUCTORS
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

#USING GETTER ASSCESSING PRIVATE VARIABLES
# class employee:
#     def __init__(self,name,perct):
#         self.__name=name
#         self.__perct=perct

#     def get_name(self):
#        return self.__name

    
#     def get_per(self):
#        return self.__perct
    
# emp1=employee("aryan",2.4)
# print("Name is ",emp1.get_name())
# print("Age is ",emp1.get_per())

#USING STRING ASSCESSING PRIVATE VARIABLES

class employee:
    def __init__(self, name, perct):
        self.__name = name
        self.__perct = perct

    def __str__(self):
        return self.get_name() + " " + str(self.get_per())

    def get_name(self):
        return self.__name

    def get_per(self):
        return self.__perct


emp1 = employee("aryan", 2.4)
print(emp1)
# print("Name is ",emp1.get_name())
# print("Age is ",emp1.get_per())





