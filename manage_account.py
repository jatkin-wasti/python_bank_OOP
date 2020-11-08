from my_account import MyAccount  # Importing our parent class so that we can inherit its functionality


class ManageAccount(MyAccount):
    def __init__(self, name, address, age):
        # Using the parent classes initialisation method to create the account and all of its attributes
        super().__init__(name, address, age)

    # Deposit method
    def deposit(self, amount):
        # Checking if they've input a number and if so, adding that value to their balance
        if str(amount).isdigit():
            self.balance += float(amount)
        else:
            # Otherwise let them know the transaction failed and why
            return "ValueError: Transaction cannot be completed due to mismatching data types."
        return self.balance

    # Withdraw method
    def withdraw(self, amount):
        # Checking if they've input a number and if so, removing that amount from their balance
        if str(amount).isdigit():
            self.balance -= float(amount)
        else:
            # Otherwise let them know the transaction failed and why
            return "ValueError: Transaction cannot be completed due to mismatching data types."
        return self.balance

    # Applying a flat 5% fee that can be run whenever necessary
    def bank_fees(self):
        self.balance -= (self.balance * 0.05)
        return self.balance


# Test calls with expected and unexpected data
new_account = ManageAccount("Jamie", "21 Jump Street", 78)
new_account.balance = 500
print(new_account.display_holder_details())
print(new_account.display_account_details())
print(new_account.withdraw("banana"))
print(new_account.balance)
new_account.withdraw(400)
print(new_account.balance)
new_account.deposit(800)
print(new_account.balance)
print(new_account.deposit("apple"))
print(new_account.balance)
new_account.bank_fees()
print(new_account.balance)
