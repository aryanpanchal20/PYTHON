
class Employee:

    def __init__(self, pid, pname, price, quantity):
        self.__pid = pid
        self.__pname = pname
        self.__price = price
        self.__quantity = quantity

    # Getter and setter for pid
    @property
    def pid(self):
        return self.__pid

    @pid.setter
    def pid(self, pid):
        self.__pid = pid

    # Getter and setter for pname
    @property
    def pname(self):
        return self.__pname

    @pname.setter
    def pname(self, pname):
        self.__pname = pname

    # Getter and setter for price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    # Getter and setter for quantity
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity


e1 = Employee(101, "Laptop", 50000, 2)

# Access using getters
print("Product ID:", e1.pid)
print("Product Name:", e1.pname)
print("Price:", e1.price)
print("Quantity:", e1.quantity)

# Modify using setters
e1.pid = 102
e1.pname = "Mobile"
e1.price = 20000
e1.quantity = 3

print("\nUpdated Product ID:", e1.pid)
print("Updated Product Name:", e1.pname)
print("Updated Price:", e1.price)
print("Updated Quantity:", e1.quantity)
