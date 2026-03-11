class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    #getter
    def get_balamce(self):
        return self.__balance
    
    #setter
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('amount must be positive.')
        else:
            self.__balance += amount
    

account = BankAccount(10_000)
print(account.get_balamce())

account.deposit(3000)
print(account.get_balamce())