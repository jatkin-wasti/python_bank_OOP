class AccountHolderDetails:
    def __init__(self, name, age):
        self.__name = name
        self.__address = ""
        self.__age = age

    # getter function for address
    @property
    def address(self):
        print("getter method called")
        return self._address

    # setter function for address
    @address.setter
    def address(self, address):
        self.__address = address

    def display_holder_details(self):
        return f"Here are the account holder details for this account:\n" \
               f"Name: {self.__name}\n" \
               f"Address: {self.__address}\n" \
               f"Age: {self.__age}"


acc_test = AccountHolderDetails("Jamie", 47)
acc_test.address = "27 Barnaby Road"
print(acc_test.display_holder_details())
