# Creating our class to hold details about the account holder
class AccountHolderDetails:
    def __init__(self, name, address, age):
        # mangling the names of the class attributes
        self.__name = name
        self.__address = address
        self.__age = age

    # getter function for name
    @property
    def name(self):
        return self.__name

    # setter function for address
    @name.setter
    def address(self, name):
        self.__name = name

    # getter function for address
    @property
    def address(self):
        return self.__address

    # setter function for address
    @address.setter
    def address(self, address):
        self.__address = address

    # getter function for age
    @property
    def age(self):
        return self.__age

    # setter function for age
    @age.setter
    def address(self, age):
        self.__age = age

    # display method to show the user their details in a nice format
    def display_holder_details(self):
        return f"Here are the account holder details for this account:\n" \
               f"Name: {self.__name}\n" \
               f"Address: {self.__address}\n" \
               f"Age: {self.__age}"


# Testing data
# acc_test = AccountHolderDetails("Jamie", "27 Barnaby Road", 47)
# acc_test.address = "29 Baker Road"
# print(acc_test.display_holder_details())
