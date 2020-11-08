from account_holder_details import AccountHolderDetails  # Importing from our Parent class
import random  # importing random so we can generate random account numbers and sort codes


# Creating a class which inherits from our parent class and holds the account details
class MyAccount(AccountHolderDetails):
    def __init__(self, name, address, age):
        super().__init__(name, address, age)
        self.__acc_num = self.__create_acc_num()
        self.__sort_code = self.__create_sort_code()
        self.__balance = 0  # The balance is originally set to 0 but this can be changed later with the setter function

    # getter function for acc_num
    @property
    def acc_num(self):
        return self.__acc_num

    # getter function for sort code
    @property
    def sort_code(self):
        return self.__sort_code

    # getter function for balance
    @property
    def balance(self):
        return self.__balance

    # setter function for balance
    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    # dunder method to randomly generate a string of 8 numbers for the users Account Number
    def __create_acc_num(self):
        generated_num = ""
        generated_num = self.generate_rand_nums(8)
        return generated_num

    # dunder method to randomly generate a string of 6 numbers separated by hyphens for the users Sort Code
    def __create_sort_code(self):
        generated_code = self.generate_rand_nums(2) + '-' + self.generate_rand_nums(2) + '-' + \
                            self.generate_rand_nums(2)
        return generated_code

    # So that we adhere to the DRY principle we'll define this function and use it to not repeat ourselves
    def generate_rand_nums(self, num):
        random_nums = ""
        for _ in range(num):
            random_nums += str(random.randint(0, 9))
        return random_nums

    # display method to show the user their account details in a nice format
    def display_account_details(self):
        return f"Here are the account details for this account:\n" \
               f"Account Number: {self.__acc_num}\n" \
               f"Sort Code: {self.__sort_code}\n" \
               f"Balance: {self.__balance}"


# Testing data
acc_test = MyAccount("Jamie","27 Barnaby Road", 67)
print(acc_test.display_account_details())
acc_test.balance = 500
print(acc_test.display_account_details())
