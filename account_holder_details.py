class AccountHolderDetails:
    def __init__(self, name, age):
        self._name = name
        self._address = ""
        self._age = age

    # getter function for address
    @property
    def address(self):
        print("getter method called")
        return self._address

    # setter function for address
    @address.setter
    def address(self, address):
        self._address = address

    def display_holder_details(self):
        return f"Here are the account holder details for this account:\n" \
               f"Name: {self._name}\n" \
               f"Address: {self._address}\n" \
               f"Age: {self._age}"


acc_test = AccountHolderDetails("Jamie", 47)
acc_test.address = "27 Barnaby Road"
print(acc_test.display_holder_details())
