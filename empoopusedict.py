class employee:

    def accept(self):
        self.eid = int(input("Enter Employee ID : "))
        self.name = input("Enter Employee Name : ")
        self.salary = int(input("Enter Salary : "))

    def calculate(self):
        self.hra = self.salary * 9 / 100
        self.ta = self.salary * 8 / 100
        self.ma = self.salary * 7 / 100

        self.finalsalary = self.salary + self.hra + self.ta + self.ma

    def show(self):
        print("============SALARY SLIP=============")
        print("   Employee ID   : ", self.eid)
        print("   Employee Name : ", self.name)
        print("   Salary        : ", self.salary)
        print("   HRA (9%)      : ", self.hra)
        print("   TA (8%)       : ", self.ta)
        print("   MA (7%)       : ", self.ma)
        print("   Final Salary  : ", self.finalsalary)
        print("=====================================")


empdict = {}

while True:

    e1 = employee()

    e1.accept()
    e1.calculate()

    empdict[e1.eid] = e1

    c = int(input("Do you want to continue? Press 1 for Yes : "))

    if c != 1:
        break


eid = int(input("Enter Employee ID to search : "))

if eid in empdict:
    empdict[eid].show()
else:
    print("Employee not found")