class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.amount += self.account_balance 
        

    def withdraw(self, amount):
        if self.account_balance < self.amount:
            self.amount -= self.account_balance
            return True
        else:
            return False
            
    
    def display_balance(self):
        print("Bank Balance: ", self.account_balance)
        



