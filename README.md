# Task
## Bank account with classes
- Create a class for the Account Holder Details with name, address, and age
- Create a class for the persons bank details that inherits from the previous class
- This class should have account number and balance
- Create a constructor() with the accountNumber and balance parameters
- Create a Deposit() method that manages the deposit action
- Create a Withdrawal() method that manages the withdrawal action
- Create a bankFees() method that applies bank fees with a percentage of 5% of the account's balance
- Create a display() method to display account details
- Create Manage Account class and import everything from the Bank Account class, call all methods the Manage Account 
class that are available from parent class
## Solution
### Account Holder Details class
- We create the class that all later classes will inherit from
- This one will set the users details when an object is created
```
class AccountHolderDetails:
    def __init__(self, name, address, age):
        # mangling the names of the class attributes
        self.__name = name
        self.__address = address
        self.__age = age
```
- These values may need to be changed later e.g. if someone changes their name or moves house. Therefore, we need to 
make getters and setters so that we can access and change these values
```
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
```
- The last thing this class needs is a method to cleanly display the users details. An fstring should work well.
```
 # display method to show the user their details in a nice format
    def display_holder_details(self):
        return f"Here are the account holder details for this account:\n" \
               f"Name: {self.__name}\n" \
               f"Address: {self.__address}\n" \
               f"Age: {self.__age}"
```
### My Account class
- Now lets have another class that inherits from our previous class and builds on it to include account details
- To do this we'll need to import the parent class at the top of the file. We'll also import random to help us 
with some methods later on
```
from account_holder_details import AccountHolderDetails  # Importing from our Parent class
import random  # importing random so we can generate random account numbers and sort codes
```
- We need to include the name of our imported parent class in the parentheses when creating this class
- Then we can use the initialising method from said parent class to deal with the users details while we can focus 
on the account details
- These details shouldn't be provided by the user so we'll assign them by calling some methods that we'll 
define soon
```
class MyAccount(AccountHolderDetails):
    def __init__(self, name, address, age):
        super().__init__(name, address, age)
        self.__acc_num = self.__create_acc_num()
        self.__sort_code = self.__create_sort_code()
        self.__balance = 0
```
- Next we'll create some getters and setters for these class variables
- We shouldn't be able to change the account number or sort code so they will only need a getter, but balance 
should have both a getter and a setter
```
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
```
- We're almost ready to create the methods we called in the initialiser, but we want these numbers to be random so let's
 create a method that randomly generates a string of numbers
- By letting the method take an argument for how many numbers to generate we can use the same block of code for all 
random number generation. This let's use adhere to the DRY principle
```
    def generate_rand_nums(self, num):
        random_nums = ""
        for _ in range(num):
            random_nums += str(random.randint(0, 9))
        return random_nums
``` 
- Finally we can create the methods called in the initialiser
- We don't want these methods to be run by a user so we'll start the method name with a double underscore to mangle the 
name
```
    # dunder method to randomly generate a string of 8 numbers for the users Account Number
    def __create_acc_num(self):
        generated_num = ""
        generated_num = self.generate_rand_nums(8)
        return generated_num
```
- We'll use basically the same function for the sort code generation but this time we'll only generate 6 numbers 
and we'll add hyphens after every 2 characters
```
    def __create_sort_code(self):
        generated_code = self.generate_rand_nums(2) + '-' + self.generate_rand_nums(2) + '-' + \
                            self.generate_rand_nums(2)
        return generated_code
``` 
- The only thing we need now is a method to display the account details
- This can be the same as the last display method we created, with the variables and headers changed
```
    def display_account_details(self):
        return f"Here are the account details for this account:\n" \
               f"Account Number: {self.__acc_num}\n" \
               f"Sort Code: {self.__sort_code}\n" \
               f"Balance: {self.__balance}"
```
### Manage Account class
- We've created classes that should handle the users personal and account details, but we can't actually do anything 
the account yet
- This means we should make a new class that inherits from MyAccount to handle this functionality
```
from my_account import MyAccount
```
- We can rely on the parent classes to deal with the data so as long as we extend the MyAccount class and call it's 
initialiser with the super() method, we can move straight on to the class methods
```
class ManageAccount(MyAccount):
    def __init__(self, name, address, age):
        # Using the parent classes initialisation method to create the account and all of its attributes
        super().__init__(name, address, age)
```
- The task says that we should allow for depositing and withdrawing money which will be very similar functions
```
    def deposit(self, amount):
        # Checking if they've input a number and if so, adding that value to their balance
        if str(amount).isdigit():
            self.balance += float(amount)
        else:
            # Otherwise let them know the transaction failed and why
            return "ValueError: Transaction cannot be completed due to mismatching data types."
        return self.balance
```
- They'll both take in an amount of money, check if the argument passed is a number, and add to or subtract that amount 
from the account's balance
```
    def withdraw(self, amount):
        # Checking if they've input a number and if so, removing that amount from their balance
        if str(amount).isdigit():
            self.balance -= float(amount)
        else:
            # Otherwise let them know the transaction failed and why
            return "ValueError: Transaction cannot be completed due to mismatching data types."
        return self.balance
```
- The last piece of functionality that was required was a method to apply a bank fee of 5% to the balance of an account
- So we'll just decrement the value of balance by 5% of its current value
```
    def bank_fees(self):
        self.balance -= (self.balance * 0.05)
        return self.balance
```
### Testing
- Here is a list of executions to test whether the programs work as intended
- We will create a new ManageAccount object with some user details to see if it initialises correctly
```
new_account = ManageAccount("Jamie", "21 Jump Street", 78)
new_account.balance = 500
print(new_account.display_holder_details())
print(new_account.display_account_details())
```
- Then we'll try to deposit and withdraw various values including strings to see if our check works
```
print(new_account.withdraw("banana"))
print(new_account.balance)
new_account.withdraw(400)
print(new_account.balance)
new_account.deposit(800)
print(new_account.balance)
print(new_account.deposit("apple"))
print(new_account.balance)
```
- Finally we'll test the bank fees method to see if the balance is reduced by 5%
```
new_account.bank_fees()
print(new_account.balance)
```
