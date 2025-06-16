class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
          amount += self.account_balance

        else:
            print("Deposit amount must be negative")
        

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        
        if amount <= self.account_balance:
            self.account_balance-= amount
            return True
        else:
            return False
            
    
    def display_balance(self):
        print("Current Balance:.2f", self.account_balance)
        



