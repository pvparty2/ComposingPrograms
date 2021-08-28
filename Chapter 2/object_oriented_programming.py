class Account():
    '''Represent a bank account with a non-negative balance.'''
    interest = 0.02 # Class Attribute
    def __init__(self, name):
        '''Construct an instance of Account data type.'''
        self.holder = name
        self.balance = 0


    def deposit(self, amount):
        '''Increate the account balance by amount and return the new balance.'''
        if amount < 0:
            return 'Cannot deposit negative int. Use withdraw instead.'
        self.balance += amount
        return self.balance

    
    def withdraw(self, amount):
        '''Decrease the account balance by amount and return the new balance.'''
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance


class CheckingAccount(Account):
    '''A bank account that charges for withdrawals.'''
    withdraw_charge = 1
    interest = 0.01
    def __init__(self, name):
        super().__init__(name)


    def withdraw(self, amount):
        return super().withdraw(amount + self.withdraw_charge)


class SavingsAccount(Account):
    deposit_charge = 2
    def __init__(self, name):
        super().__init__(name)


    def deposit(self, amount):
        return super().deposit(amount - self.deposit_charge)    

# Multiple Inheritance
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, name):
        super().__init__(name)
        self.holder = name
        self.balance = 1

[c.__name__ for c in AsSeenOnTVAccount.mro()]