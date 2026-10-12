
class Account:

    def __init__(self, accno, name, acctype, accbal):
        self.__details = [accno, name, acctype, accbal]

    @property
    def accno(self):
        return self.__details[0]

    @accno.setter
    def accno(self, accno):
        self.__details[0] = accno

    @property
    def name(self):
        return self.__details[1]

    @name.setter
    def name(self, name):
        self.__details[1] = name

    @property
    def acctype(self):
        return self.__details[2]

    @acctype.setter
    def acctype(self, acctype):
        self.__details[2] = acctype

    @property
    def accbal(self):
        return self.__details[3]

    @accbal.setter
    def accbal(self, accbal):
        self.__details[3] = accbal


accounts = []

while True:
    print("\n1.Create 2.Read 3.Update 4.Delete 5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        accno = int(input("Enter account number: "))
        name = input("Enter name: ")
        acctype = input("Enter account type: ")
        accbal = float(input("Enter balance: "))

        a = Account(accno, name, acctype, accbal)
        accounts.append(a)
        print("Account created")

    elif ch == 2:
        for a in accounts:
            print(a.accno, a.name, a.acctype, a.accbal)

    elif ch == 3:
        accno = int(input("Enter account number: "))

        for a in accounts:
            if a.accno == accno:
                a.name = input("Enter new name: ")
                a.acctype = input("Enter new account type: ")
                a.accbal = float(input("Enter new balance: "))
                print("Account updated")
                break
        else:
            print("Account not found")

    elif ch == 4:
        accno = int(input("Enter account number: "))

        for a in accounts:
            if a.accno == accno:
                accounts.remove(a)
                print("Account deleted")
                break
        else:
            print("Account not found")

    elif ch == 5:
        break

    else:
        print("Invalid choice")
