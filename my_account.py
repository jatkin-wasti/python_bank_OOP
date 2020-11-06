from account_holder_details import AccountHolderDetails


class MyAccount(AccountHolderDetails):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._acc_num = ""
        self._sort_code = ""
        self._balance = 0


    # getter function for acc_num
    @property
    def acc_num(self):
        print("getter method called")
        return self._acc_num

    # setter function for name
    @acc_num.setter
    def acc_num(self, acc_num):
        self._acc_num = acc_num

    # getter function for sort code
    @property
    def sort_code(self):
        print("getter method called")
        return self._sort_code

    # setter function for sort code
    @sort_code.setter
    def sort_code(self, sort_code):
        self._sort_code = sort_code

    # getter function for balance
    @property
    def balance(self):
        print("getter method called")
        return self._balance

    # setter function for balance
    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def display_account_details(self):
        return f"Here are the account details for this account:\n" \
               f"Account Number: {self._acc_num}\n" \
               f"Sort Code: {self._sort_code}\n" \
               f"Balance: {self._balance}"


acc_test = MyAccount("Jamie", 67)
print(acc_test.display_account_details())
acc_test.acc_num = "192837"
acc_test.sort_code = "75-12-80"
acc_test.balance = 500
print(acc_test.display_account_details())
