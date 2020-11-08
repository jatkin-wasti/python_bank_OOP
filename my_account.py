from account_holder_details import AccountHolderDetails
import random


class MyAccount(AccountHolderDetails):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__acc_num = self.__create_acc_num()
        self.__sort_code = self.__create_sort_code()
        self.__balance = 0

    # getter function for acc_num
    @property
    def acc_num(self):
        print("getter method called")
        return self.__acc_num

    # setter function for name
    @acc_num.setter
    def acc_num(self, acc_num):
        self.__acc_num = acc_num

    # getter function for sort code
    @property
    def sort_code(self):
        print("getter method called")
        return self.__sort_code

    # setter function for sort code
    @sort_code.setter
    def sort_code(self, sort_code):
        self.__sort_code = sort_code

    # getter function for balance
    @property
    def balance(self):
        print("getter method called")
        return self.__balance

    # setter function for balance
    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def __create_acc_num(self):
        generated_num = ""
        for _ in range(7):
            generated_num += str(random.randint(0, 9))
        return generated_num

    def __create_sort_code(self):
        generated_code = self.generate_rand_nums() + '-' + self.generate_rand_nums() + '-' + \
                            self.generate_rand_nums()
        return generated_code

    def generate_rand_nums(self):
        return str(random.randint(0, 9)) + str(random.randint(0, 9))

    def display_account_details(self):
        return f"Here are the account details for this account:\n" \
               f"Account Number: {self.__acc_num}\n" \
               f"Sort Code: {self.__sort_code}\n" \
               f"Balance: {self.__balance}"


acc_test = MyAccount("Jamie", 67)
print(acc_test.display_account_details())
acc_test.balance = 500
print(acc_test.display_account_details())
