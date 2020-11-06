from my_account import MyAccount


class ManageAccount(MyAccount):
    def __init__(self, name, address, age, acc_num, sort_code, balance):
        super().__init__(name, address, age, acc_num, sort_code, balance)

    def deposit(self, amount):
        if str(amount).isdigit():
            self.balance += float(amount)
        return self.balance

    def withdraw(self, amount):
        if str(amount).isdigit():
            self.balance -= float(amount)
        return self.balance

    def bank_fees(self):
        return self.balance - (self.balance*0.05)

    def display_holder_details(self):
        return f"Here are the account holder details for this account:\n" \
               f"Name: {self.name}\n" \
               f"Address: {self.address}\n" \
               f"Age: {self.age}"

    def display_account_details(self):
        return f"Here are the account details for this account:\n" \
               f"Account Number: {self.acc_num}\n" \
               f"Sort Code: {self.sort_code}\n" \
               f"Balance: {self.balance}"


new_account = ManageAccount("Jamie", "21 Jump Street", 78, "11223344", "00-34-29", 500.00)
print(new_account.display_holder_details())
print(new_account.display_account_details())
new_account.withdraw("banana")
print(new_account.display_account_details())
new_account.withdraw(400)
print(new_account.display_account_details())
