from account_holder_details import AccountHolderDetails


class MyAccount(AccountHolderDetails):
    def __init__(self, name, address, age, acc_num, sort_code, balance):
        super().__init__(name, address, age)
        self.acc_num = acc_num
        self.sort_code = sort_code
        self.balance = balance

