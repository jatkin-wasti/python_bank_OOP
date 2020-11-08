from my_account import MyAccount


class ManageAccount(MyAccount):
    def __init__(self, name, address, age, balance):
        super().__init__(name, address, age, balance)

    def deposit(self, amount):
        if str(amount).isdigit():
            self.balance += float(amount)
        return self.balance

    def withdraw(self, amount):
        if str(amount).isdigit():
            self.balance -= float(amount)
        return self.balance

    def bank_fees(self):
        self.balance -= (self.balance * 0.05)
        return self.balance


new_account = ManageAccount("Jamie", "21 Jump Street", 78, "11223344", "00-34-29", 500.00)
print(new_account.display_holder_details())
print(new_account.display_account_details())
new_account.withdraw("banana")
print(new_account.balance)
new_account.withdraw(400)
print(new_account.balance)
new_account.deposit(800)
print(new_account.balance)
new_account.deposit("apple")
print(new_account.balance)
new_account.bank_fees()
print(new_account.balance)
