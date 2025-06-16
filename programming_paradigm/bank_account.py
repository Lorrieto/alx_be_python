class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
          amount += self.account_balance

        else:
            print("Deposit amount must be negative")
        

    def withdraw(self, amount):
        
        if self.account_balance < self.amount:
            self.amount -= self.account_balance
            return True
        else:
            return False
            
    
    def display_balance(self):
        print("Current Balance:", self.account_balance)
        



